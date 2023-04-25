import utils
from tables import Spec
from config import SESSIONFACTORY, ENGINE


session = SESSIONFACTORY()
Spec.__table__.create(ENGINE, checkfirst=True)
spec1 = Spec(name='test1', headbuild='headbuild info', audio_config='audio config info', colorspace='colorsapce info')
spec1.headbuild = str('new headbuild info')
# session.add(spec1)
# session.commit()

spec = session.query(Spec).filter(Spec.name == 'test1').first()
if spec:
    print(spec.name, spec.headbuild, spec.audio_config, spec.colorspace, spec.created, spec.updated)

# update headbuild on spec1

# result = session.query(Spec).all()
# for r in result:
#     print(r.headbuild)

session.close()