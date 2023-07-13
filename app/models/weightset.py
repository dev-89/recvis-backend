from beanie import Document


class WeightSet(Document):
    weightset_id: int
    user_id: int
    user_mail: str
    weight_name: str
    text_weight: float
    citation_weight: float
    image_weight: float
    formula_weight: float
