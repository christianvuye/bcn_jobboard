from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Union


class JobPosting(BaseModel):
    title: str
    description: str
    hiring_organization: str # create a custom Company type in the future? 
    job_location: list[str]
    date_posted: datetime
    valid_through: Optional[datetime]
    employment_type: str # enum in the future? 
    base_salary: Optional[Union[int, str]]
    requirements: list[str] # list of bullet points
    experience_years: int 
    education_requirements: str # future enum like BACHELOR OR MASTER