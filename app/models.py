import uuid
from pydantic import BaseModel
from sqlalchemy import Column, String, Date, Float, Integer, Double, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cif_number = Column(String(32), nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    gender = Column(String(16), nullable=False)
    birth_date = Column(Date, nullable=False) 
    nationality = Column(String(24), nullable=True)


class CustomerIdentification(Base):
    __tablename__ = "customer_identifications"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id: uuid.UUID = Column(UUID(as_uuid=True) )
    document_type = Column(String(16))
    document_number = Column(Double, nullable=False)
    issued_date = Column(String, nullable=False)
    expiry_date = Column(String, nullable=False)

class CustomerContacts(Base):
    __tablename__ = "customer_contacts"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id: uuid.UUID = Column(UUID(as_uuid=True) )
    email = Column(String(16))
    phone = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    country_iso2 = Column(String, nullable=False)


class CustomerAccounts(Base):
    __tablename__ = "customer_accounts"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id: uuid.UUID = Column(UUID(as_uuid=True) )
    account_type = Column(String(16))
    currency = Column(String, nullable=False)
    balance = Column(Double, nullable=False)
    status = Column(String, nullable=False)
    opened_date = Column(Date, nullable=False)
    closed_date = Column(Date, nullable=False)


class CustomerLoans(Base):
    __tablename__ = "customer_loans"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id: uuid.UUID = Column(UUID(as_uuid=True) )
    loan_type = Column(String(16))
    loan_amount = Column(Float, nullable=False)
    # still in debt
    out_balance = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    loan_status = Column(String, nullable=False)
    # The disbursement date in a loan is the specific date the loan funds are released and paid out to the borrower
    disbursement_date = Column(Date, nullable=False)


class CustomerTransactions(Base):
    __tablename__ = "customer_transactions"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id: uuid.UUID = Column(UUID(as_uuid=True) )
    created_at = Column(Date, nullable=False)
    type = Column(String(16))
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    description = Column(String(128), nullable=False)

class CustomerCards(Base):
    __tablename__ = "customer_cards"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id: uuid.UUID = Column(UUID(as_uuid=True) )
    card_type = Column(String(16))
    card_number = Column(String(16))
    expiry_date = Column(Date, nullable=False)
    credit_limit = Column(Float, nullable=False)
    outstanding_balance = Column(String, nullable=False)
    status = Column(String(128), nullable=False)

class CustomerOnBoardIntention(Base):
    __tablename__ = "customer_onboard_intentions"
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(Date, nullable=False)
    payload = Column(MutableDict.as_mutable(JSON), nullable=False)
    current_step = Column(Integer, nullable=False)
    status = Column(String(128), nullable=False)
    

# class Branch(Base):
#     __tablename__ = "branches"
#     id: uuid.UUID = Column(
#         UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = Column(String(128), nullable=False)
#     address = Column(String(128), nullable=False)
#     phone_number = Column(String(24), nullable=False)
#     manager_name = Column(String(64), nullable=False)
