from mongoengine import Document, StringField, DictField, EmailField, DecimalField, EmbeddedDocument, ListField, EmbeddedDocumentField
# from background_task import background

class Food(EmbeddedDocument):
    foodId = StringField()
    label = StringField()
    knownAs = StringField()
    nutrients = DictField(
    field=DecimalField(),
    required=True,
    default={
        "ENERC_KCAL": 0,
        "PROCNT": 0,
        "FAT": 0,
        "CHOCDF": 0,
        "FIBTG": 0
    }
)
    category = StringField()
    categoryLabel = StringField()
    image = StringField()