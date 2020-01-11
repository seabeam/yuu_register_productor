{% for key, block in root %}

class block_{{ module }}_{{ block.name }} extends uvm_reg_block;
  {% for key, reg in block %}
  rand reg_{{ module }}_{{ reg.name }} {{ reg.name }};
  {% endfor %}

  {% if factory %}
  `uvm_object_utils_begin(block_{{ module }}_{{ block.name }})
  {% for key, reg in block %}
    `uvm_field_object({{ reg.name }}, UVM_ALL_ON)
  {% endfor %}
  `uvm_object_utils_end
  {% endif %}

  function new(string name="block_{{ module }}_{{ block.name  }}");
    super.new(name, {{ coverage }});
  endfunction

  function void build();
    default_map = create_map("default_map", {{ block.width }}'h{{ block.offset }}, {{ (block.width/8)|int }}, UVM_LITTLE_ENDIAN);
    {% for key, reg in block %}

    {% if factory %}
    {{ reg.name }} = reg_{{ module }}_{{ reg.name }}::type_id::create("{{ reg.name }}");
    {% else %}
    {{ reg.name }} = new("{{ reg.name }}");
    {% endif %}
    {{ reg.name }}.configure(this, null, "");
    {{ reg.name }}.build();
    default_map.add_reg({{ reg.name }}, {{ block.width }}'h{{ reg.offset }}, "{{ reg.access.upper() }}");
    {% endfor %}
  endfunction
endclass : block_{{ module }}_{{ block.name }}
{% endfor %}
