#! /usr/bin/python
# -*- coding: UTF-8 -*-

#
#       pyshut.py
#       Copyright 2010 wkt <weikting@gmail.com>
#       本示例仅在ylmf os 3.0/kubuntu 10.04测试通过
#       可以自由传播/复制,但是有关版权说明还是不要修改了吧!

import dbus
import os,sys
import glib

if __name__ == "__main__":
   if len(sys.argv) < 2:
      print >> sys.stderr, "Usage:"
      print >> sys.stderr, "   %s stop|restart " % os.path.basename(sys.argv[0])
      sys.exit(1)

   try:
      bus = dbus.SystemBus()
      obj = bus.get_object('org.freedesktop.ConsoleKit','/org/freedesktop/ConsoleKit/Manager')
      iface = dbus.Interface(obj, 'org.freedesktop.ConsoleKit.Manager')
   except:
      type ,err, obj = sys.exc_info()
      print >> sys.stderr,err
      sys.exit(2)

   if sys.argv[1].upper() == 'restart'.upper():
      if iface.CanRestart():
         iface.Restart()
      else:
         print >>sys.stderr, "Can't support restart"
   elif sys.argv[1].upper() == 'stop'.upper() \
       or sys.argv[1].upper() == 'halt'.upper() \
       or sys.argv[1].upper() == 'shutdown'.upper() :
      if iface.CanStop():
         iface.Stop()
      else:
         print >> sys.stderr, "Can't support %s" % sys.argv[1].lower()
