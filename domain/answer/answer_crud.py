from datetime import datetime

from sqlalchemy.orm import Session

from domain.answer import answer_schema
from domain.answer.answer_schema import AnswerCreate
from models import Answer, Question, User


def create_answer(
    db: Session, question: Question, answer_create: AnswerCreate, user: User
):
    db_answer = Answer(
        question_id=question.id,
        content=answer_create.content,
        create_date=datetime.now(),
        user=user,
    )
    db.add(db_answer)
    db.commit()


def get_answer(db: Session, answer_id: int):
    return db.get(Answer, answer_id)


def update_answer(
    db: Session, answer_update: answer_schema.AnswerUpdate, db_answer: Answer
):
    db_answer.content = answer_update.content
    db_answer.modify_date = datetime.now()
    db.add(db_answer)
    db.commit()


def delete_answer(db: Session, db_answer: Answer):
    db.delete(db_answer)
    db.commit()


def vote_answer(db: Session, db_answer: Answer, db_user: User):
    db_answer.voter.append(db_user)
    db.commit()
