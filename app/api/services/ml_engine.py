# Cosine Similarity & TF-IDF implementation

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(student, active_projects):
    # 1. Prepare text data for projects
    proj_data = [{
        "id": p.project_id,
        "content": f"{p.category} {p.required_skills}"
    } for p in active_projects]
    
    df_projects = pd.DataFrame(proj_data)
    
    # 2. Prepare student content
    student_content = f"{student.department} {student.skills}"

    # 3. Apply TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    all_docs = df_projects['content'].tolist() + [student_content]
    tfidf_matrix = tfidf.fit_transform(all_docs)

    # 4. Calculate Cosine Similarity
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # 5. Rank and return top 5
    df_projects['similarity_score'] = cosine_sim[0]
    results = df_projects.sort_values(by='similarity_score', ascending=False)
    
    return results.head(5)['id'].tolist()