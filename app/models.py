from app import db


class User(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    sd_gender = db.Column("Пол", db.String(70))
    sd_age_estimated = db.Column("Предполагаемый возраст", db.String(70))
    sd_living_country = db.Column("Страна проживания", db.String(70))
    sd_job_profession = db.Column("Профессия", db.String(70))
    sd_job_pos_category = db.Column("Категория занимаемой должности", db.String(70))
    fin_acc_balance_avg_3m = db.Column("Средний остаток по всем счетам за последние 3 месяца", db.Integer)
    sd_marital_status = db.Column("Семейное положение", db.String(70))
    sd_children = db.Column("Дети", db.String(70))
    real_estate_owner_type = db.Column("Наличие жилья определенного типа", db.String(70))
    leisure_hobby = db.Column("Наличие хобби", db.String(70))
    consumerelectronics_owner_type = db.Column("Владелец потребительской электроники определенного типа", db.String(70))
    consumerelectronics_interest_type = db.Column("Интерес к потребительской электронике определенного типа",
                                                  db.String(70))
    car_owner_count = db.Column("Наличие автомобиля", db.String(70))
    insurance_user = db.Column("Владелец страхового продукта", db.String(70))
    insurance_interest = db.Column("Интерес к страховому продукту", db.String(70))

    def __repr__(self):
        return '<User {}>'.format(self.id)
