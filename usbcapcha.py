import wmi

raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI ()
watcher = c.watch_for(raw_wql=raw_wql)
while 1:
  usb = watcher ()
  print(usb)