from math import (sin,cos,tan, radians)
angulo = float(input('Digete o angulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O seu angulo de {:.0f}º detém o SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}.'.format(angulo,seno, cos, tan))