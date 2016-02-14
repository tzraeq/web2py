# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## db.define_table('account',
##  Field('accnum','integer'),
##  Field('acctype'),
##  Field('accdesc'),
##  primarykey=['accnum','acctype'],
##  migrate=False)
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('region',Field('name','string',length=32),Field('displayName','string'),Field('status','string'))
db.define_table('service',Field('name','string',length=64),Field('region','reference region'))
db.define_table('portMapping',Field('protocol','string'),Field('url','string'),Field('port','integer'),Field('service','reference service'),rname='port_mapping')

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
