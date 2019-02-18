{% for key, node in root %}
  {% for rkey, reg in node %}

class reg_{{ module }}_{{ reg.name }} extends uvm_reg;
    {% for fkey, field in reg %}
  rand uvm_reg_field {{ field.name }};
    {% endfor %}

  function new(string name="reg_{{ module }}_{{ reg.name }}",
               int unsigned n_bits,
               int has_coverage
               );
    super.new(name, n_bits, has_coverage);
  endfunction : new

  virtual function void build();
    {% for fkey, field in reg %}
    
    {{ field.name }} = new("{{ field.name }}");
    {{ field.name }}.configure(.parent(this), .size({{ field.size }}), .lsb_pos({{ field.lsb_pos }}),
                               .access("{{ field.access.upper() }}"), .volatile(0), .reset({{ field.reset }}),
                               .has_reset(1), .is_rand(0), .individually_accessible(0));
    {% endfor %}
  endfunction : build
endclass : reg_{{ module }}_{{ reg.name }}
  {% endfor %}
{% endfor %}
