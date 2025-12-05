# api/utils/beneficiary_json.py

def decimal_to_float(value):
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return value


def beneficiary_to_json(beneficiary):
    """
    Build a JSON-ready dict with ALL data for a Beneficiary:
    - Beneficiary basic fields
    - CaseDetails
    - LoanHistory
    - ConsumptionData
    - Documents
    - LoanApplication
    - AIScoreLog
    """
    data = {}

    # 1. Beneficiary basic fields
    data["beneficiary"] = {
        "id": beneficiary.id,
        "name": beneficiary.name,
        "age": beneficiary.age,
        "gender": beneficiary.gender,
        "date_of_birth": beneficiary.date_of_birth.isoformat() if beneficiary.date_of_birth else None,
        "phone": beneficiary.phone,
        "email": beneficiary.email,
        "location": beneficiary.location,
        "location_type": beneficiary.location_type,
        "state": beneficiary.state,
        "district": beneficiary.district,
        "pincode": beneficiary.pincode,
        "household_size": beneficiary.household_size,
        "education_level": beneficiary.education_level,
        "marital_status": beneficiary.marital_status,
        "ration_card_type": beneficiary.ration_card_type,
        "govt_subsidy_received": beneficiary.govt_subsidy_received,
        "aadhaar_verified": beneficiary.aadhaar_verified,
        "pan_available": beneficiary.pan_available,
        "bank_account_active": beneficiary.bank_account_active,
        "income_est": beneficiary.income_est,
        "estimated_monthly_income": beneficiary.estimated_monthly_income,
        "income_category": beneficiary.income_category,
        "employment_type": beneficiary.employment_type,
        "work_consistency_days": beneficiary.work_consistency_days,
        "eligibility_label": beneficiary.eligibility_label,
        "model_score": beneficiary.model_score,
        "approval_flag": beneficiary.approval_flag,
        "other_details": beneficiary.other_details,
        "risk_band": beneficiary.risk_band,
        "need_band": beneficiary.need_band,
        "score": beneficiary.score,
        "eligibility": beneficiary.eligibility,
        "number_of_loans": beneficiary.number_of_loans,
        "emi_due_delays": beneficiary.emi_due_delays,
        "credit_card_available": beneficiary.credit_card_available,
        "cibil_score": beneficiary.cibil_score,
        "case_type": beneficiary.case_type,
        "loans_dues_change_reason": beneficiary.loans_dues_change_reason,
        "otp_code": beneficiary.otp_code,
        "otp_created_at": beneficiary.otp_created_at.isoformat() if beneficiary.otp_created_at else None,
        "is_phone_verified": beneficiary.is_phone_verified,
        "created_at": beneficiary.created_at.isoformat() if beneficiary.created_at else None,
        "updated_at": beneficiary.updated_at.isoformat() if beneficiary.updated_at else None,
    }

    # 2. CaseDetails (OneToOne)
    if hasattr(beneficiary, "case_details"):
        cd = beneficiary.case_details
        data["case_details"] = {
            "case_type": cd.case_type,
            "electricity_units": cd.electricity_units,
            "electricity_bill": decimal_to_float(cd.electricity_bill),
            "payments_regularity": cd.payments_regularity,
            "average_mobile_bill": decimal_to_float(cd.average_mobile_bill),
            "gas_bill": decimal_to_float(cd.gas_bill),
            "gas_frequency": cd.gas_frequency,
            "employment_type": cd.employment_type,
            "working_days_per_month": cd.working_days_per_month,
            "digital_payment_frequency": cd.digital_payment_frequency,
            "average_bank_balance": decimal_to_float(cd.average_bank_balance),
            "cash_inflow": decimal_to_float(cd.cash_inflow),
            "cash_outflow": decimal_to_float(cd.cash_outflow),
            "transactions_per_month": cd.transactions_per_month,
            "last_6_months_avg_bank_balance": decimal_to_float(cd.last_6_months_avg_bank_balance),
            "number_of_active_loans": cd.number_of_active_loans,
            "total_properties_value": decimal_to_float(cd.total_properties_value),
            "wealth_index": decimal_to_float(cd.wealth_index),
            "any_business": cd.any_business,
            "insurance_coverage": cd.insurance_coverage,
            "luxury_expenditures": decimal_to_float(cd.luxury_expenditures),
            "outstanding_bank_balance": decimal_to_float(cd.outstanding_bank_balance),
            "loan_purpose": cd.loan_purpose,
            "loan_history_cibil": cd.loan_history_cibil,
            "reasons_for_delay": cd.reasons_for_delay,
            "total_emi_per_month": decimal_to_float(cd.total_emi_per_month),
            "number_of_due_delays": cd.number_of_due_delays,
            "created_at": cd.created_at.isoformat() if cd.created_at else None,
        }

    # 3. LoanHistory (beneficiary.loans)
    data["loan_history"] = [
        {
            "id": str(l.id),
            "amount": l.amount,
            "tenure": l.tenure,
            "repayment_status": l.repayment_status,
            "created_at": l.created_at.isoformat() if l.created_at else None,
        }
        for l in beneficiary.loans.all()
    ]

    # 4. ConsumptionData (beneficiary.consumption_records)
    data["consumption"] = [
    {
        "id": str(c.id),
        "electricity_bill": c.electricity_bill,
        "mobile_bill": c.mobile_bill,
        "other_bills": c.other_bills,
        "created_at": c.created_at.isoformat() if c.created_at else None,
    }
    for c in beneficiary.consumption_records.all()
]

    

    # 5. BeneficiaryDocument (beneficiary.documents)
    data["documents"] = [
        {
            "doc_type": d.doc_type,
            "document_number": d.document_number,
            "image": d.image.url if d.image else None,
            "uploaded_at": d.uploaded_at.isoformat() if d.uploaded_at else None,
        }
        for d in beneficiary.documents.all()
    ]

    # 6. LoanApplication (beneficiary.loan_applications)
    data["loan_applications"] = [
        {
            "id": la.id,
            "loan_amount": decimal_to_float(la.loan_amount),
            "tenure_months": la.tenure_months,
            "phone": la.phone,
            "email": la.email,
            "status": la.status,
            "decision_notes": la.decision_notes,
            "created_at": la.created_at.isoformat() if la.created_at else None,
            "updated_at": la.updated_at.isoformat() if la.updated_at else None,
        }
        for la in beneficiary.loan_applications.all()
    ]

    # 7. AIScoreLog (beneficiary.ai_logs)
    data["ai_score_logs"] = [
        {
            "id": str(log.id),
            "score": log.score,
            "risk_band": log.risk_band,
            "need_band": log.need_band,
            "explanation": log.explanation,
            "model_used": log.model_used,
            "created_at": log.created_at.isoformat() if log.created_at else None,
        }
        for log in beneficiary.ai_logs.all()
    ]

    return data
