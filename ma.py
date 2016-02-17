import win32com.client
o = win32com.client.Dispatch("Excel.Application")
o.Visible = 1
o.Worbooks.Add()
o.Cells(1,1).Value = "hello"
#print o.property

,
	options={
       "py2exe":{
            "skip_archive": True
                }
        }


#excel = win32.gencache.EnsureDispatch('Excel.Application')