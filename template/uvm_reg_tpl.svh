{% for key, node in root %}
  {% for rkey, reg in node %}

class reg_{{ module }}_{{ reg.name }} extends uvm_reg;
    {% for fkey, field in reg %}
  rand uvm_reg_field {{ field.name }};
    {% endfor %}

  function void new(string name="reg_{{ module }}_{{ reg.name }}");
    super.new(name);
  endfunction : new

  virtual function void build();
    {% for fkey, field in reg %}
    
    {{ field.name }} = new("{{ field.name }}");
    {{ field.name }}.configure(.parent(this), .size({{ field.size }}),
                    .access("{{ field.access.upper() }}"), .has_reset(1), .is_rand(0),
                    .indevidually_access(0));
    {% endfor %}
  endfunction : build
endclass : reg_{{ module }}_{{ reg.name }}
  {% endfor %}
{% endfor %}
