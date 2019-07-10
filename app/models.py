from app import db


class User(db.Model):
    id = db.Column(db.String(120), primary_key=True)
    sd_gender = db.Column("Пол", db.String(200))
    sd_age_estimated = db.Column("Предполагаемый возраст", db.String(200))
    sd_living_country = db.Column("Страна проживания", db.String(200))
    sd_job_profession = db.Column("Профессия", db.String(200))
    sd_job_pos_category = db.Column("Категория занимаемой должности", db.String(200))
    fin_acc_balance_avg_3m = db.Column("Ср.ост. по всем сч. за последн. 3 мес.", db.Integer)
    sd_marital_status = db.Column("Семейное положение", db.String(200))
    sd_children = db.Column("Дети", db.String(200))
    real_estate_owner_type = db.Column("Наличие жилья опред. типа", db.String(200))
    leisure_hobby = db.Column("Наличие хобби", db.String(200))
    consumerelectronics_owner_type = db.Column("Владелец потреб. электрон.", db.String(200))
    consumerelectronics_interest_type = db.Column("Интерес к потреб. электрон.", db.String(200))
    car_owner_count = db.Column("Наличие автомобиля", db.String(200))
    insurance_user = db.Column("Владелец страхового продукта", db.String(200))
    insurance_interest = db.Column("Интерес к страховому продукту", db.String(200))

    def __repr__(self):
        return '<User {}>'.format(self.id)
