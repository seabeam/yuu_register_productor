{% for key, block in root %}

class block_{{ module }}_{{ block.name }} extends uvm_reg_block;
  {% for key, reg in block %}
  rand reg_{{ module }}_{{ reg.name }} {{ reg.name }};
  {% endfor %}

  function new(string name="block_{{ module }}_{{ block.name  }}");
    super.new(name);
  endfunction

  function void build();
    default_map = create_map("default_map", {{ block.width }}'h{{ block.offset }}, {{ (block.width/8)|int }}, UVM_LITTLE_ENDIAN);
    {% for key, reg in block %}

    {{ reg.name }} = new("{{ reg.name }}", {{ width }}, UVM_NO_COVERAGE);
    {{ reg.name }}.configure(this, null, "");
    {{ reg.name }}.build();
    default_map.add_reg({{ reg.name }}, {{ block.width }}'h{{ reg.offset }}, "{{ reg.access.upper() }}");
    {% endfor %}
  endfunction
endclass : block_{{ module }}_{{ block.name }}
{% endfor %}
