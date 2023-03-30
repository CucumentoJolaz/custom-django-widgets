from django.forms import DateTimeInput, DateInput, SelectMultiple, CheckboxSelectMultiple


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/xdsoft_datetimepicker.html'


class BootstrapDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/bootstrap_datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id = f'datetimepicker_{name}'
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context


class FengyuanChenDatePickerInput(DateInput):
    template_name = 'widgets/fengyuanchen_datepicker.html'


class CheckboxSelectMultipleWithLinksInput(CheckboxSelectMultiple):
    template_name = 'widgets/select_multiple_with_links.html'
    option_template_name = 'widgets/checkbox_option_with_links.html'


    def __init__(self, queryset=None, *args, **kwargs):
        super().__init__()
        self.queryset = queryset


    def optgroups(self, name, value, attrs=None):
        """Return a list of optgroups for this widget."""
        groups = []
        has_selected = False

        ids = [choice[0] for choice in self.choices]
        if self.queryset:
            instances = self.queryset
        else:
            instances = [None for _ in ids]
        choices_with_models = [(choice[0], choice[1], instance) for choice, instance in zip(self.choices, instances)]

        for index, (option_value, option_label, instance) in enumerate(choices_with_models):
            if option_value is None:
                option_value = ''

            subgroup = []
            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subindex = 0
                choices = option_label
            else:
                group_name = None
                subindex = None
                choices = [(option_value, option_label)]
            groups.append((group_name, subgroup, index))

            for subvalue, sublabel in choices:
                selected = (
                    str(subvalue) in value and
                    (not has_selected or self.allow_multiple_selected)
                )
                has_selected |= selected
                subgroup.append(self.create_option(
                    name, subvalue, sublabel, selected, index,
                    subindex=subindex, attrs=attrs, instance=instance
                ))
                if subindex is not None:
                    subindex += 1
        return groups

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None, instance=None):
        option = super(CheckboxSelectMultiple, self).create_option(name, value, label, selected, index, subindex, attrs)
        option['instance'] = instance
        return option
