import datos_web as dw
pais = input("País para copnsultar la hora: ")
ciudad = input("Ciudad para consultar la hora: ")
url = "https://www.timeanddate.com/worldclock/" + pais + "/" + ciudad
parser = '//span[@class = \'h1\']/text()'
web = dw.GetWebData(url)
print("La hora en ", ciudad, " de ", pais, "es:",
      web.get_data(parser))
