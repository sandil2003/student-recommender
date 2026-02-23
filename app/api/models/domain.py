# Table definitions (User, Student_Profile, Project)

from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentProfile(Base):
    __tablename__ = "Student_Profile"
    student_id = Column(Integer, primary_key=True) 
    department = Column(String(255))
    skills = Column(Text)

class Project(Base):
    __tablename__ = "Project"
    project_id = Column(Integer, primary_key=True) 
    title = Column(String(255))
    category = Column(Enum('Research', 'Startup', 'Product'))
    required_skills = Column(Text)
    status = Column(Enum('Active', 'Completed'))