total_segs = int(input())


horas = total_segs // 3600

segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print("%d:%d:%d"%(horas,minutos,segs_restantes_final))