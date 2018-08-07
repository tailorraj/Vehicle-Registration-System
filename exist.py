from flask import Flask, flash, redirect, render_template,request, url_for, session
import Dbfun
import os
import datetime


lis1=Dbfun.available_timeslot('08/10/2018','Two Wheeler')
print lis1





