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
    option_template_name = 'django/forms/widgets/checkbox_option.html'
