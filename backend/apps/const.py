"""性別"""
SEX_UNKNOWN = "UNKNOWN"
SEX_MALE = "male"
SEX_FEMALE = "female"
SEX_SET = (
        (SEX_UNKNOWN, "不明"),
        (SEX_MALE, "男性"),
        (SEX_FEMALE, "女性"),
)

"""職業"""
JOB_DOCTOR = "DOCTOR"
JOB_NURSE = "NURSE"
JOB_PHARMACIST = "PHARMACIST"
JOB_PHYSICAL = "PHYSICAL"
JOB_OCCUPATIONAL = "OCCUPATIONAL"
JOB_CLERK = "CLERK"
JOB_SET = (
        (JOB_DOCTOR, "医師"),
        (JOB_NURSE, "看護師"),
        (JOB_PHARMACIST, "薬剤師"),
        (JOB_PHYSICAL, "理学療法士"),
        (JOB_OCCUPATIONAL, "作業療法士"),
        (JOB_CLERK, "事務員"),
)