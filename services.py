from sqlalchemy.orm import Session
from models import Student, Enrollment, Group

def get_student_enrollments_with_join(session: Session, student_id: int):
    """Consulta optimizada con JOIN para evitar el problema N+1."""
    return session.query(Enrollment).join(Student).filter(Student.id == student_id).all()

def enroll_student(session: Session, student_id: int, group_id: int):
    enrollment = Enrollment(student_id=student_id, group_id=group_id, status="ACTIVE")
    session.add(enrollment)
    session.commit()
    return enrollment