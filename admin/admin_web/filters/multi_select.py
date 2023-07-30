from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class MultiSelectRelatedFieldListFilter(admin.RelatedFieldListFilter):

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        # self.lookup_kwarg = "%s__%s__in" % (field_path, field.target_field.name)
        self.lookup_kwarg = "%s__in" % field_path
        self.lookup_kwarg_isnull = "%s__isnull" % field_path
        values = params.get(self.lookup_kwarg, [])
        self.lookup_val = values.split(",") if values else []
        self.custom_filter_id = [int(v) for v in self.lookup_val]
        self.lookup_choices = self.field_choices(field, request, model_admin)

    def choices(self, changelist):
        yield {
            "selected": self.lookup_val is None and not self.lookup_val_isnull,
            "query_string": changelist.get_query_string(
                remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
            ),
            "display": _("All"),
        }

        for pk_val, val in self.lookup_choices:
            if val is None:
                self.include_empty_choice = True
                continue
            val = str(val)

            if str(pk_val) in self.lookup_val:
                values = [str(v) for v in self.lookup_val if str(v) != str(pk_val)]
            else:
                values = self.lookup_val + [str(pk_val)]

            yield {
                "selected": self.lookup_val is not None and str(pk_val) in self.lookup_val,
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: ",".join(values)}, [self.lookup_kwarg_isnull]
                ),
                "display": val,
            }
