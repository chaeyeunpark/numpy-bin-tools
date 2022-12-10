import numpy as np
import pytest
from numpy_bin_tools import walsh_hadamard 

@pytest.mark.parametrize("test_input,expected", [
    ([0.45911, 0.06643], [0.37161, 0.27766]),
    ([0.00926, 0.77846], [0.55700, -0.54390]),
    ([0.80206, 0.42789, 0.00756, 0.93609], [1.08680, -0.27718, 0.14315, 0.65135]),
    ([0.93557, 0.84028, 0.02006, 0.47350], [1.13470, -0.17908, 0.64114, 0.27437]),
    ([0.92458, 0.85850, 0.84210, 0.30891, 0.81491, 0.01743, 0.28592, 0.00841], [1.43570, 0.59194, 0.41368, 0.01869, 0.63902, -0.16819, 0.03326, -0.34899]),
    ([0.88199, 0.64291, 0.82032, 0.68536, 0.19342, 0.79710, 0.81798, 0.67236], [1.94859, -0.02971, -0.16993, -0.22810, 0.19435, 0.29419, 0.18351, 0.30173]),
    ([0.63888, 0.11013, 0.01502, 0.33579, 0.63472, 0.32499, 0.58730, 0.43710, 0.34856, 0.18321, 0.67496, 0.00327, 0.78413, 0.75579, 0.64567, 0.05556], [1.63377, 0.53085, 0.25643, -0.01476, -0.47886, -0.00834, -0.13057, 0.18635, -0.09180, -0.19689, -0.08968, 0.51929, 0.03672, -0.11763, 0.36201, 0.15864]),
    ([0.93837, 0.91883, 0.80311, 0.45531, 0.06458, 0.78631, 0.62013, 0.01815, 0.27995, 0.42916, 0.37252, 0.67679, 0.83606, 0.36411, 0.15452, 0.78880], [2.12668, -0.09206, 0.18201, -0.09767, 0.31035, 0.04898, -0.05272, 0.01107, 0.17572, 0.21585, 0.22368, -0.72831, 0.50288, 0.19456, 0.24581, 0.48665]),
])
def test_transfrom_real(test_input, expected):
    assert np.allclose(walsh_hadamard(test_input), expected, atol=1e-4)


@pytest.mark.parametrize("test_input,expected", [
    ([0.74949 + 0.97355j, 0.62507 + 0.00179j], [0.97196 + 0.68967j, 0.08798 + 0.68714j]),
    ([0.77770 + 0.10568j, 0.45620 + 0.10096j], [0.87250 + 0.14611j, 0.22733 + 0.00333j]),
    ([0.20443 + 0.00686j, 0.50594 + 0.39880j, 0.48977 + 0.69250j, 0.06622 + 0.22982j], [0.63318 + 0.66399j, 0.06102 + 0.03538j, 0.07719 + -0.25833j, -0.36254 + -0.42731j]),
    ([0.14317 + 0.92935j, 0.79605 + 0.52655j, 0.28538 + 0.87355j, 0.18678 + 0.32368j], [0.70569 + 1.32656j, -0.27714 + 0.47633j, 0.23353 + 0.12934j, -0.37574 + -0.07354j]),
    ([0.41362 + 0.32731j, 0.85915 + 0.97026j, 0.18822 + 0.58117j, 0.22392 + 0.92654j, 0.97106 + 0.64902j, 0.18764 + 0.41432j, 0.55797 + 0.97545j, 0.37944 + 0.03469j], [1.33680 + 1.72490j, 0.16996 + 0.06617j, 0.38251 + -0.05549j, 0.06896 + -0.35484j, -0.14538 + 0.25873j, -0.51024 + -0.76501j, 0.22604 + -0.09310j, -0.35876 + 0.14442j]),
    ([0.61098 + 0.75905j, 0.96014 + 0.16522j, 0.75896 + 0.72582j, 0.88671 + 0.56790j, 0.57401 + 0.30825j, 0.42108 + 0.81795j, 0.53780 + 0.70162j, 0.58935 + 0.06428j], [1.88763 + 1.45314j, -0.13277 + 0.31091j, -0.07305 + -0.00324j, -0.00599 + -0.25143j, 0.38698 + 0.11522j, -0.20446 + 0.22066j, 0.02033 + -0.25801j, -0.15058 + 0.55966j]),
    ([0.31623 + 0.63306j, 0.31420 + 0.74673j, 0.20659 + 0.52573j, 0.91049 + 0.96427j, 0.29656 + 0.55038j, 0.23965 + 0.96472j, 0.72458 + 0.59243j, 0.70756 + 0.81648j, 0.05045 + 0.04533j, 0.75544 + 0.79439j, 0.04542 + 0.29442j, 0.37740 + 0.60194j, 0.27659 + 0.41172j, 0.78424 + 0.80285j, 0.17781 + 0.27602j, 0.34670 + 0.02790j], [1.63248 + 2.26209j, -0.58536 + -0.59754j, -0.11580 + 0.21250j, 0.00851 + -0.23656j, -0.14437 + 0.04084j, -0.28405 + -0.20684j, 0.06400 + -0.29592j, 0.15795 + 0.17822j, 0.22545 + 0.63481j, 0.27140 + 0.00225j, -0.57549 + -0.21451j, 0.36440 + 0.30384j, 0.03395 + -0.06795j, -0.10384 + 0.24994j, 0.14063 + 0.18772j, 0.17507 + 0.07937j]),
    ([0.05596 + 0.01072j, 0.54974 + 0.23496j, 0.15213 + 0.53824j, 0.06861 + 0.78845j, 0.96717 + 0.05960j, 0.60570 + 0.30163j, 0.78713 + 0.35571j, 0.86224 + 0.21180j, 0.79566 + 0.45560j, 0.02263 + 0.09431j, 0.30344 + 0.09257j, 0.32620 + 0.30808j, 0.33952 + 0.75135j, 0.11004 + 0.64667j, 0.81660 + 0.84442j, 0.85182 + 0.05686j], [1.90365 + 1.43774j, 0.20515 + 0.11636j, -0.18044 + -0.16032j, 0.22995 + -0.11651j, -0.76646 + -0.17628j, -0.03516 + -0.28070j, 0.46724 + -0.30555j, -0.12069 + 0.41790j, 0.12070 + -0.18718j, -0.26711 + -0.40264j, 0.33467 + -0.48332j, -0.30030 + -0.06348j, -0.43144 + 0.49809j, -0.31316 + 0.09253j, -0.23652 + -0.13181j, -0.38625 + -0.21194j]),
])
def test_transfrom_cmplx(test_input, expected):
    assert np.allclose(walsh_hadamard(test_input), expected, atol=1e-4)

