from marshmallow import Schema, fields


class ImageResultSchema(Schema):
    name = fields.Str()
    tags = fields.List(fields.Str())
    created_at = fields.Str()  # we'll get iso strings from search
    image_type = fields.Str()
    image_url = fields.Url()
    published = fields.Boolean()


class AutoCompleteSchema(Schema):
    text = fields.Str()
    result = fields.Nested(ImageResultSchema(), attribute='_source')