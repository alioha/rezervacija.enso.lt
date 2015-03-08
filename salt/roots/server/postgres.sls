{% set app = salt['pillar.get']('app') %}

include:
  - pkgs.postgres

{{ app.db_user }}:
  postgres_user.present:
    - password: {{ app.db_password }}
    - superuser: True
    - inherit: True

{{ app.db_name }}:
  postgres_database.present:
    - owner: {{ app.db_user }}
