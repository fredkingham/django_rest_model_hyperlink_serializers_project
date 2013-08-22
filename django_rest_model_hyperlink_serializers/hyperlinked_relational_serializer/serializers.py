from rest_framework.relations import HyperlinkedRelatedField
from rest_framework import serializers
from django.core.exceptions import ValidationError

FIELD_KEYS = ["data", "partial", "context", "instance", "files"]


class HyperLinkedRelationalSerializerOptions(serializers.HyperlinkedModelSerializerOptions):
    """
    Options for HyperlinkedModelSerializer
    """
    def __init__(self, meta):
        self._queryset = getattr(meta, 'queryset', None)
        setattr(meta, 'model', self.queryset.model)
        super(HyperLinkedRelationalSerializerOptions, self).__init__(meta)

    @property
    def queryset(self):
        return self._queryset


class HyperLinkedRelationalSerializer(serializers.HyperlinkedModelSerializer):
    _options_class = HyperLinkedRelationalSerializerOptions


    def __init__(self, *args, **kwargs):
        super(HyperLinkedRelationalSerializer, self).__init__(*args, **kwargs)
        hyperlink_args = {key: value for key, value in kwargs.items() if key not in FIELD_KEYS}
        hyperlink_args["view_name"] = self.opts.view_name
        hyperlink_args["queryset"] = self.opts.queryset
        self.hyperlinked_related_field = HyperlinkedRelatedField(**hyperlink_args)


    def initialize(self, *args, **kwargs):
        self.hyperlinked_related_field.initialize(**kwargs)
        return super(HyperLinkedRelationalSerializer, self).initialize(**kwargs)


    def field_from_native(self, data, files, field_name, into):
        """
        Override default so that the serializer can be used as a writable
        nested field across relationships.
        """
        if self.read_only:
            return

        data_fields = data.get(field_name, None)

        if not data_fields and self.required:
            raise ValidationError("%s is required" % field_name)

        if data_fields:
            if self.many:
                into[field_name] = []

                for data_field in data_fields:
                    if isinstance(data_field, str) or isinstance(data_field, unicode):
                        into[field_name].append(self.hyperlinked_related_field.from_native(data_field))
                    else:
                        into[field_name].append(super(HyperLinkedRelationalSerializer, self).field_from_native(data, files, field_name, into))
            else:
                if isinstance(data_field, str) or isinstance(data_field, unicode):
                    into[field_name] = self.hyperlinked_related_field.from_native(data_field)