def lanzarTablaHTML(dataframe,nombretabla):
    fileHTML=dataframe.to_html()
    file=open(f"./tablas/{nombretabla}.html","w",encoding='utf-8')
    file.write(fileHTML)
    file.close()