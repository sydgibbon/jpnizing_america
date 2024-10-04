from classes.models import User, Plan, Level, Class, UserLevel
from werkzeug.security import generate_password_hash
from db import db_session

def seed_database():

    # Inserción de usuarios
    admin = User(
        username='admin',
        email='admin@example.com',
        password=generate_password_hash('admin123'),
        is_admin=True
    )
    student = User(
        username='student1',
        email='student1@example.com',
        password=generate_password_hash('student123'),
        is_admin=False
    )

    db_session.add(admin)
    db_session.add(student)
    
    db_session.commit()


    # Inserción de planes
    basic_plan = Plan(name='Básico', description='Acceso a clases de nivel N5 y N4', access_level=1)
    medium_plan = Plan(name='Mediano', description='Acceso a clases de nivel N5, N4, y N3', access_level=2)
    advanced_plan = Plan(name='Avanzado', description='Acceso a todas las clases (N5, N4, N3, N2, y N1)', access_level=3)

    db_session.add(basic_plan)
    db_session.add(medium_plan)
    db_session.add(advanced_plan)
    
    db_session.commit()


    # Inserción de secciones (Niveles)
    level_n5 = Level(level='N5')
    level_n4 = Level(level='N4')
    level_n3 = Level(level='N3')
    level_n2 = Level(level='N2')
    level_n1 = Level(level='N1')

    db_session.add(level_n5)
    db_session.add(level_n4)
    db_session.add(level_n3)
    db_session.add(level_n2)
    db_session.add(level_n1)
    
    db_session.commit()


    # Inserción de clases con URLs de ejemplo
    class1 = Class(title='Introducción al nivel N5', video_url='https://www.youtube.com/watch?v=example1', level_id=1)
    class2 = Class(title='Gramática básica N5', video_url='https://www.youtube.com/watch?v=example2', level_id=1)
    class3 = Class(title='Introducción al nivel N4', video_url='https://www.youtube.com/watch?v=example3', level_id=2)
    class4 = Class(title='Kanji avanzado N4', video_url='https://www.youtube.com/watch?v=example4', level_id=2)
    class5 = Class(title='Introducción al nivel N3', video_url='https://www.youtube.com/watch?v=example5', level_id=3)
    class6 = Class(title='Lectura intermedia N3', video_url='https://www.youtube.com/watch?v=example6', level_id=3)
    class7 = Class(title='Conversación nivel N2', video_url='https://www.youtube.com/watch?v=example7', level_id=4)
    class8 = Class(title='Gramática avanzada N2', video_url='https://www.youtube.com/watch?v=example8', level_id=4)
    class9 = Class(title='Nivel experto N1', video_url='https://www.youtube.com/watch?v=example9', level_id=5)
    class10 = Class(title='Comprensión lectora N1', video_url='https://www.youtube.com/watch?v=example10', level_id=5)

    db_session.add(class1)
    db_session.add(class2)
    db_session.add(class3)
    db_session.add(class4)
    db_session.add(class5)
    db_session.add(class6)
    db_session.add(class7)
    db_session.add(class8)
    db_session.add(class9)
    db_session.add(class10)
    
    db_session.commit()


    # Asignar acceso a clases según plan
    user1_level_access = [
        UserLevel(user_id=1, level_id=1, access_granted=True),
        UserLevel(user_id=1, level_id=2, access_granted=True),
    ]

    user2_level_access = [
        UserLevel(user_id=2, level_id=1, access_granted=True),
        UserLevel(user_id=2, level_id=2, access_granted=True),
        UserLevel(user_id=2, level_id=3, access_granted=True),
        UserLevel(user_id=2, level_id=4, access_granted=True),
        UserLevel(user_id=2, level_id=5, access_granted=True)
    ]

    db_session.bulk_save_objects(user1_level_access)
    db_session.bulk_save_objects(user2_level_access)

    # Guardar todo en la base de datos
    db_session.commit()

