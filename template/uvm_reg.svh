{% for key, block in root %}
  {% for rkey, reg in block %}

class reg_{{ module }}_{{ reg.name }} extends uvm_reg;
  {% for fkey, field in reg %}
  rand uvm_reg_field {{ field.name }};
  {% endfor %}

  {% if factory %}
  `uvm_object_utils_begin(reg_{{ module }}_{{ reg.name }})
  {% for fkey, field in reg %}
    `uvm_field_object({{ field.name }}, UVM_ALL_ON)
  {% endfor %}
  `uvm_object_utils_end
  {% endif %}

  function new(string name="reg_{{ module }}_{{ reg.name }}");
    super.new(name, {{ block.width }}, {{ coverage }});
  endfunction

  virtual function void build();
    {% for fkey, field in reg %}
    {% if factory %}
    {{ field.name }} = uvm_reg_field::type_id::create("{{ field.name }}");
    {% else %}
    {{ field.name }} = new("{{ field.name }}");
    {% endif %}
    {{ field.name }}.configure(.parent(this), .size({{ field.size }}), .lsb_pos({{ field.lsb_pos }}),
                               .access("{{ field.access.upper() }}"), .volatile({{ field.is_volatile }}), .reset({{ block.width }}'h{{ field.reset }}),
                               .has_reset({{ field.has_reset }}), .is_rand({{ field.is_rand }}), .individually_accessible(0));
    {% endfor %}
  endfunction
endclass : reg_{{ module }}_{{ reg.name }}
  {% endfor %}
{% endfor %}
