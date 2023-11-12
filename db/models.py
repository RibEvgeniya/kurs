import datetime
from enum import Enum

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, Boolean,Float, Integer, Column, Text, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass
class Employee(SQLAlchemyBaseUserTable[int],Base):
    __tablename__ = "employee"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(75), nullable=False)
    last_name: Mapped[str] = mapped_column(String(75), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(75), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(    String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(   String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(   Boolean, default=True, nullable=False )
    ##region: Mapped[str]=mapped_column(String(20),nullable=True)
    specialisation: Mapped["Specialisation"] = relationship()
    specialisation_id: Mapped[int] = mapped_column(ForeignKey("specialisation.id"))
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))
    birthdate: Mapped[datetime.date] = mapped_column(nullable=False)
    salary: Mapped[float] = mapped_column(nullable=False)
    education: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)

class Region(Base):
    __tablename__ = "region"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    area: Mapped[str] = mapped_column(String(50), nullable=True)

class Specialisation(Base):
    __tablename__ = "specialisation"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    employees: Mapped[list[Employee]] = relationship(back_populates="specialisation")
    oklad: Mapped[float] = mapped_column(nullable=False)
    procedure_id: Mapped[int] = mapped_column(ForeignKey("procedure.id"))

class Patient(SQLAlchemyBaseUserTable[int],Base):
    __tablename__ = "patient"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(75), nullable=False)
    last_name: Mapped[str] = mapped_column(String(75), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(75), nullable=True)
    email: Mapped[str] = mapped_column( String(length=320), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(12), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(  Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    birthdate:Mapped[datetime.date]=mapped_column(nullable=False)
    polis: Mapped[str] = mapped_column(String(75), nullable=False)
    adress: Mapped[str] = mapped_column(String(75), nullable=False)
    ##med_data: Mapped["Med_data"]=relationship()
    ##med_data_id: Mapped[int] = mapped_column(ForeignKey("med_data.id"))
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"))

class Med_data(Base):
    __tablename__="med_data"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    blood_type: Mapped[str] = mapped_column(String(75), nullable=True)
    height: Mapped[float] = mapped_column(Float, nullable=True)
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    ##all_diagnos: Mapped[list[Diagnos]] = relationship(back_populates="specialisation")
    norm_presure: Mapped[str] = mapped_column(String(75), nullable=True)
    sugar: Mapped[str] = mapped_column(String(75), nullable=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analysis.id"))
    hr_ill_id: Mapped[int] = mapped_column(ForeignKey("hronolog_illness.id"))
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    ##all_photo:

class Hronolog_illness(Base):
    __tablename__="hronolog_illness"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))



class Photo(Base):
    __tablename__ = "photo"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc: Mapped[str] = mapped_column(String(200), nullable=True)
    rentgen: Mapped[str] = mapped_column(String(20), nullable=True)
    EKG: Mapped[str] = mapped_column(String(20), nullable=True)
    fluragraf: Mapped[str] = mapped_column(String(20), nullable=True)

class Blank(Base):
    __tablename__ = "blank"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc: Mapped[str] = mapped_column(String(200), nullable=True)
    type: Mapped[str] = mapped_column(String(20), nullable=True)
    blank: Mapped[str] = mapped_column(String(20), nullable=True)

class Analysis(Base):
    __tablename__="analysis"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    blood: Mapped[str] = mapped_column(String(20), nullable=True)
    sugar: Mapped[str] = mapped_column(String(20), nullable=True)
    urin: Mapped[str] = mapped_column(String(20), nullable=True)
    ##rentgen: Mapped[str] = mapped_column(String(20), nullable=True)
    ##EKG: Mapped[str] = mapped_column(String(20), nullable=True)
    ##fluragraf: Mapped[str] = mapped_column(String(20), nullable=True)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    ##photo_id: Mapped[int] = mapped_column(ForeignKey("photos.id"))
    desc: Mapped[str] = mapped_column(String(200), nullable=True)
    photo_id: Mapped[int] = mapped_column(ForeignKey("photo.id"))
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))


class Illness(Base):
    __tablename__="illness"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=True)
    desc: Mapped[str] = mapped_column(String(200), nullable=True)
    symptoms: Mapped[str] = mapped_column(String(200), nullable=True)
    MKB10_code: Mapped[str] = mapped_column(String(10), nullable=True)
    treatment: Mapped[str] = mapped_column(String(200), nullable=True)

class Medicine(Base):
    __tablename__ = "medicine"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=True)
    desc: Mapped[str] = mapped_column(String(1000), nullable=True)
    contraindications: Mapped[str] = mapped_column(String(1000), nullable=True)
    producer: Mapped[str] = mapped_column(String(50), nullable=True)
    release_form: Mapped[str] = mapped_column(String(1000), nullable=True)

class Procedure(Base):
    __tablename__ = "procedure"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(75), nullable=True)
    desc: Mapped[str] = mapped_column(String(1000), nullable=True)
    indications: Mapped[str] = mapped_column(String(1000), nullable=True)
    contraindications: Mapped[str] = mapped_column(String(1000), nullable=True)
    price: Mapped[float] = mapped_column(nullable=True)


class Examination(Base):
    __tablename__ = "examination"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    outdoors: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    desc: Mapped[str] = mapped_column(String(1000), nullable=True)
    ##adress: Mapped[int] = mapped_column(ForeignKey("patient.adress"))  можно достать через ай ди пациента через результат
    result_id: Mapped[int] = mapped_column(ForeignKey("result.id"))
    diagnos_id: Mapped[int] = mapped_column(ForeignKey("diagnos.id"))
class Diagnos(Base):
    __tablename__ = "diagnos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    illness: Mapped["Illness"]=relationship()
    illness_id: Mapped[int]=mapped_column(ForeignKey("illness.id"))
    medicine_id: Mapped[int] = mapped_column(ForeignKey("medicine.id"))

class Result(Base):
    __tablename__ = "result"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    emp_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    diag_id: Mapped[int] = mapped_column(ForeignKey("diagnos.id"))
    proc_id:  Mapped[int] = mapped_column(ForeignKey("procedure.id"))
    res_price: Mapped[float] = mapped_column(nullable=True)



class Reception(Base):
    __tablename__="reception"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_open: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    desc: Mapped[str] = mapped_column(String(200), nullable=True)



class Schedule(Base):
    __tablename__="schedule"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    is_open: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    emp_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))
    date: Mapped[datetime.date]=mapped_column(nullable=False)
    time: Mapped[datetime.time]=mapped_column(nullable=False)
    cabinet: Mapped[str] = mapped_column(String(10), nullable=True)
    desc: Mapped[str] = mapped_column(String(200), nullable=True)

class Pol_polis(Base):
    __tablename__ = "policlinic_polis"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    polis: Mapped[str] = mapped_column(String(75), nullable=False)

class Pat_Emp(Base):
    __tablename__ = "patient_employee"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    emp_id: Mapped[int] = mapped_column(ForeignKey("employee.id"))

class Pat_Diag(Base):
    __tablename__ = "patient_diagnos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pat_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    diag_id: Mapped[int] = mapped_column(ForeignKey("diagnos.id"))





class PermissionsEnum(Enum):
    EMPLOYEES_CREATE = "employees:create"
    EMPLOYEES_READ = "employees:read"
    EMPLOYEES_UPDATE = "employees:update"
    EMPLOYEES_DELETE = "employees:delete"

    PATIENT_CREATE = "clients:create"
    PATIENT_READ = "clients:read"
    PATIENT_UPDATE = "clients:update"
    PATIENT_DELETE = "clients:delete"

    BOOKING_CREATE = "booking:create"
    BOOKING_READ = "booking:read"
    BOOKING_UPDATE = "booking:update"
    BOOKING_DELETE = "booking:delete"

    SERVICES_CREATE = "services:create"
    SERVICES_READ = "services:read"
    SERVICES_UPDATE = "services:update"
    SERVICES_DELETE = "services:delete"

    ROOMS_CREATE = "rooms:create"
    ROOMS_READ = "rooms:read"
    ROOMS_UPDATE = "rooms:update"
    ROOMS_DELETE = "rooms:delete"

    SERVICE_ORDERS_CREATE = "service_orders:create"
    SERVICE_ORDERS_READ = "service_orders:read"
    SERVICE_ORDERS_UPDATE = "service_orders:update"
    SERVICE_ORDERS_DELETE = "service_orders:delete"
