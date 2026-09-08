# CREATE TABLE

# USERS = [id, username, telegram_id]
# QUESTIONS = [id, question_text, correct_answer]
# RESULTS = [id, user_id, question_id, is_correct]


CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        telegram_id INTEGER NOT NULL UNIQUE
    )
'''

CREATE_QUESTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
'''

CREATE_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,

        FOREING KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREING KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
'''