import utils
from tables import Spec
from config import SESSIONFACTORY, ENGINE


session = SESSIONFACTORY()
utils.delete_table(Spec.__tablename__, ENGINE)
# Spec.__table__.create(ENGINE, checkfirst=True)
# spec1 = Spec(name='test1', headbuild='headbuild info', audio_config='audio config info', colorspace='colorsapce info')

# spec = session.query(Spec).one()
# spec.audio_config = ['ch1', 'ch2', 'ch3']
# spec.start_timecode = None
# session.commit()
# session.close()