#!/bin/sh

cd eqobject
exec gunicorn -b :15000 main:app