from beanie import Document


class ResearchDisciplineWeightSet(Document):
    weightset_id = str
    weight_name = str
    text_weight = float
    citation_weight = float
    image_weight = float
    formula_weight = float
