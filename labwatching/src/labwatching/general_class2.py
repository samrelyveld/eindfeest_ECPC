'''import nidaqmx
from nidaqmx.constants import AcquisitionType'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fft import fft, fftfreq
from lmfit import models

class datafiles:
    def __init__(self):
         self.data = []
    
    def datainput(self):
        self.data = [1.8006369836305602, 0.44443567474387635, -1.1830543203038488, -2.449829035216025, -2.591441522093968, -1.6051508237874466, -0.4202197292606524, 1.0298973367591675, 2.1570099977593955, 2.5037183362109703, 1.6725557948388607, 0.5639766011995856, -1.1994870798804935, -2.4722228091003196, -2.592408160738161, -1.6346331515842727, -0.2768357037342392, 0.9677100162370644, 2.0700109898526735, 2.592973499955796, 1.7059052155747403, 0.42026973174022875, -1.0781746531627325, -2.434201727442858, -2.534248748144217, -1.5680965355185277, -0.2421979792788482, 0.782276018867672, 2.0282837280476316, 2.5448014722062484, 2.0704943173605117, 0.29315693645569724, -1.2636070658316025, -2.4303351773247486, -2.535215386375451, -1.7042307883956673, -0.42408626390123777, 0.8124029808566208, 1.9789843705418253, 2.6021568007796834, 1.7766318133586088, 0.5575323437047552, -1.2769788222765406, -2.340437915274562, -2.457239924028166, -1.5373253684927712, -0.2995516044204492, 1.1283338214602328, 2.30877521269955, 2.339386075180361, 1.7212105101571855, 0.43766921029174033, -1.0340317531207082, -2.2060754360819073, -2.3670204334599974, -1.5603634671330664, -0.20482145299004278, 0.8694347918609706, 2.288153166448215, 2.532557083561639, 1.794998184544178, 0.35228290020425024, -1.1266674017274232, -2.5534204076817444, -2.5310266207562058, -1.5796961383968766, -0.3217841863484931, 1.0331194787475475, 1.9519180715695292, 2.4271910021013428, 1.765998653169958, 0.4389580606388173, -1.0654473206254917, -2.4081025161181575, -2.432268452371025, -1.4902825417970904, -0.08479765588088017, 1.0759739770025152, 2.2133983052418538, 2.3292361559486614, 1.8926300245854366, 0.7070392013173085, -1.1316616715762349, -2.4520845230750354, -2.597241354065869, -1.4727220359006343, -0.12217420057239269, 1.2275759433936426, 2.074522046727673, 2.6282567164256476, 1.8090146287846112, 0.46199626256620074, -0.9971385995961327, -2.6165741291652402, -2.3981139302840107, -1.6194892233279101, -0.182266650021582, 0.8947285705517842, 2.2643089339086937, 2.708006533168819, 1.6432340938305847, 0.4299361084531365, -1.0847799776631457, -2.378136760608251, -2.541820747805857, -1.4694999248017682, -0.41023118124026176, 1.2095319134431994, 2.1476656543815458, 2.600384584716821, 1.5910350488909253, 0.3477719266941056, -1.1123290141700304, -2.68230558631226, -2.4989664573558668, -1.5341032569028887, -0.21803212237455447, 1.0468135833435548, 2.1392879683470785, 2.6637010654872153, 1.949662547129429, 0.4792346399028139, -1.0146990962510642, -2.350426497330603, -2.4822114000242124, -1.1857931135507789, -0.38123216919479996, 1.0311861935422306, 2.2179093719666945, 2.5008183512264037, 1.8699136936060976, 0.46876272818308845, -1.3900748930180502, -2.490911141081571, -2.4746394036141766, -1.3831473553258162, -0.16776713275337138, 1.0735573694691605, 1.959006863140925, 2.4826128931857423, 1.7864594324615568, 0.49051208417661113, -0.9818335795559691, -2.5095994755496753, -2.45514554236869, -1.6749095599053063, -0.344016766626141, 1.1202784589482244, 2.1400935150347427, 2.6007068058150873, 1.8206144467296663, 0.3575994048705194, -1.1964260756279872, -2.5503593862289224, -2.5663089198265125, -1.6747484542619375, -0.2304372625278627, 1.0211975539012355, 2.0203893841036775, 2.6691788305062003, 1.685444458139552, 0.4478189070906131, -1.0860688214697918, -2.43645721505901, -2.4151911903424743, -1.3372322820058702, -0.2396202879804992, 0.8857065851242255, 2.279614352407104, 2.5837902005986795, 1.8270587908267248, 0.58379269498181, -1.1426168441981306, -2.3929585314046014, -2.4607842622906793, -1.547313914588545, -0.50753895999182, 0.8583184196294041, 2.261247850653942, 2.419779939151681, 1.7407046266804203, 0.49002876511742816, -1.231869283301966, -2.5500371734484553, 
        -2.528932237994728, -1.6761984050552343, -0.12829622024416434, 1.0706574405067335, 1.9754399736482589, 2.5939401631312786, 1.6148790527853334, 0.34197210380594206, -1.0291985889013118, -2.5672755582873585, -2.4799559116895153, -1.6608933692393502, -0.412003343006881, 0.9185723927977387, 2.181820847010665, 2.5868513002216407, 1.8368864166705927, 0.568487581633928, -0.9004753141002769, -2.416802252713462, -2.4042359666837183, -1.5023654591078517, -0.18919419686219371, 1.0907958378305531, 2.2220982199237205, 2.3691914032062633, 1.779853983412866, 0.5786372881796795, -1.2123755189318564, -2.4739949784064628, -2.630590392916058, -1.5724463865553926, -0.4967448864184502, 1.0864459436614122, 2.0577666941447443, 2.737973160347461, 2.0104006236852427, 0.41012003688719995, -1.03258180385468, -2.5018663713282048, -2.528287812536106, -1.7849447347115053, -0.24397014203210962, 0.9712543702885656, 2.091921840374147, 2.620362296237549, 1.584912940937806, 0.5201556564006945, -1.0664139534748922, -2.5991746314468487, -2.5481038967817886, -1.6040230845227816, -0.36705487349012333, 0.8059587102448313, 2.2235482058187737, 2.552856992453922, 1.7049385654939189, 0.33649449350245403, -1.2033536115798513, -2.4229242898834777, -2.441451509190437, -1.5160594324759369, -0.34997767555725917, 0.905522732673077, 2.1359046723666055, 2.4930850586307396, 1.7903260370560556, 0.5662320913973723, -1.012282514143133, -2.581614029613966, -2.6164130226941946, -1.5002710867496043, -0.4376191348100929, 1.0244196956136882, 2.2763921587304203, 2.5178960426356354, 1.6545116698310618, 0.6126307555767666, -1.0591642071098182, -2.4835002505173467, -2.520071388203988, -1.4984989255314265, -0.23704259665733218, 1.0405304057100493, 2.2132371957218266, 2.524984897130843, 2.1521767165354406, 0.3353667502289616, -1.0905797747976518, -2.299194744455878, -2.661361735965189, -1.3915248427785412, -0.3000349214368056, 0.9949371027297577, 2.3917467962037438, 2.5391626086955954, 1.82834765971437, 0.5235388905981353, -0.9265744015075391, -2.519104750079547, -2.520715813624051, -1.5769573432400161, -0.36995477493484064, 1.0808071922458709, 2.150243404145754, 2.4326687448671773, 1.8639526717740973, 0.5283720824560415, -1.0983128376630875, -2.542787386090889, -2.472706127999804, -1.5837237783706193, -0.2757079639365214, 0.9999314211470653, 2.13364914180956, 2.2493257383342296, 1.8546083682726944, 0.4357359347929268, -1.0556198866689297, -2.3787811853953267, -2.5858027968110027, -1.5349087847979133, -0.017294311285685645, 0.9245333491845698, 2.167482108304093, 2.4816462318533525, 1.664339273108602, 0.47182374845057623, -1.1029848964892288, -2.4401626590755954, -2.444190315722447, -1.8121716001806867, -0.19934385816806777, 1.0974012330473732, 2.1694154212038423, 2.625195614590266, 1.7548821691386969, 0.6835176364021328, -1.2152754177399183, -2.495099905486384, -2.5487483223342706, -1.7350019708237734, -0.3092179445953507, 1.0203920184890498, 2.3419638327106154, 2.6092456655790497, 1.7307159051889034, 0.338588873889493, -0.8943533058920866, -2.4698062146275204, -2.5049273916977857, -1.5060708871516097, -0.27087479332349007, 0.9026228084153831, 2.0973995541260093, 2.5033961156500872, 1.7978981383061845, 0.563493281876527, -1.027265323214056, -2.6378401851112865, -2.2352356291823994, -1.6660487496422594, -0.022288592882904645, 0.7721262954827977, 2.280419900852033, 2.6110178819160046, 1.9698011607816397, 0.6670847649744986, -1.0952518336094106, -2.29951695668661, -2.4472513348488456, -1.618039272785549, -0.1785612179116294, 0.9061671602964654, 1.9090631195865038, 2.476329594806635, 1.8625026935652411, 0.3767710444674822, -1.2500742041061965, -2.339793490647746, -2.388286451322779, -1.7333909140717285, -0.11411891128479287, 1.0904736234410726, 
        2.213076086202203, 2.6849676856042124, 1.841236349844797, 0.6214916134890115, -1.1234452921547597, -2.4134190217546383, -2.602880079840264, -1.826026692573451, -0.2837632481069848, 1.0442358693952352, 2.3351972194228257, 2.39029680640321, 1.7864594324615568, 0.29299583031800464, -0.9914999080055511, -2.3091833239085053, -2.4517623105215898, -1.5284645616831225, -0.21964317957050775, 0.8003199737585522, 2.205665048735827, 2.4975961458551605, 1.8165867319573543, 0.49002876511742816, -1.142455738717874, -2.2755121472475945, -2.6815000535416464, -1.4319623321372308, -0.13667372058840668, 0.8555796034540669, 1.8852190221971745, 2.705106537847614, 1.748115614449673, 0.495023062144124, -1.2961503770957459, -2.244740886573048, -2.40294711689452, -1.59935102189334, -0.2028881842427582, 1.2191983576235375, 2.2375647378320083, 2.717350963564473, 1.8518695209237643, 0.36597692775466073, -1.19255954395236, -2.370242557187831, -2.529093344359858, -1.5303978286066886, -0.3068013595815748, 1.2082430542949505, 2.1391268590107297, 2.5900735105268446, 1.8918244808103273, 0.6300302589721278, -1.1170010730256743, -2.328838272396949, -2.3510709220014028, -1.680870468768248, -0.1292628549145166, 1.0518079043064128, 2.320375116707591, 2.540129270972993, 1.7313603387936152, 0.6092475190820258, -1.19255954395236, -2.519104750079547, -2.5585758123911284, -1.6355997853258808, -0.16647828673266316, 1.0382749061422087, 2.1842374886773146, 2.7014009884899792, 1.9725400126882329, 0.5783150752613313, -1.2563573184520793, -2.303544609625107, -2.4875279083842905, -1.678292778435181, -0.31340669190557247, 0.8956952118919697, 2.1513711696994715, 2.6016734691207453, 1.8188422522025487, 0.6353467743760763, -0.9070806387229329, -2.43645721505901, -2.4625564314547823, -1.4559670584335391, -0.12571852777036524, 1.1869768809112586, 2.1679654365236534, 2.4191354989381946, 1.8807079776412545, 0.5175779542118776, -1.0449869253604505, -2.4752838288248142, -2.5555147908211038, -1.7335520197465277, -0.25331427272067625, 0.912289222910633, 2.1581377634296954, 2.301686383534234, 1.6654670309414614, 0.36501029047501415, -1.0080937718225502, -2.418896633821992, -2.38329215898144, -1.6594434185159923, -0.30664025391328215, 0.9662600532506106, 2.236436970774639, 2.258186767547177, 1.7556877114042728, 0.6007088749933224, -0.8650321083647098, -2.4420959342521447, -2.5550314716322062, -1.680226046182982, -0.44164677486267284, 0.9449939317482376, 1.9491792204731544, 2.727017617351202, 1.6728780113951067, 0.39272056163958324, -1.1498665908266117, -2.497516500392283, -2.6202795780546704, -1.4450118811836272, -0.3688270354872281, 0.8892509364530675, 1.9747955378688915, 2.6081178915750134, 1.7987036810380852, 0.28171840108492757, -0.795273432415715, -2.449506822667614, -2.4921999916543442, -1.7565901321795434, -0.24831999601344368, 0.9664211602481138, 2.204859501236549, 2.606023454197876, 1.780015091919249, 0.41527543735873335, -1.1575996539349267, -2.5593813443948314, -2.5901526705794313, -1.660732263603098, -0.3995982104475255, 0.9367774768600182, 2.0240948923718305, 2.568968036300033, 1.4724595667417684, 0.6285803002645205, -1.0583586797366578, -2.530059982554617, -2.397469505414399, -1.7955777114254088, -0.34450008357076606, 0.9920371760177351, 2.179565314869659, 2.504846108187931, 1.90455207352181, 0.5251499545314979, -0.9687840361250766, -2.4583676680112925, -2.7528702775542793, -1.6898923851027268, -0.27458022413427463, 1.189071276560959, 2.006050680087156, 2.5892679579336337, 1.6781945847674988, 0.5058171885969324, -1.140844683916188, -2.5584147059909674, -2.4280796898030133, -1.684898109956456, -0.2969739136529395, 0.9770542226323635, 2.112060496090711, 2.270269991198428, 1.6720724700070138, 0.5361051897903317, -0.9633064499830899, -2.3177219487730225, -2.458045455443781, -1.6281889267114455, -0.33821696323160055, 1.0373082634856932, 2.06340551426016, 2.6102123290287667, 1.9361294020136899, 0.41672539377433215, -1.0312929600628111
        -2.4847891010222494, -2.4116468531879915, -1.4917324918565187, -0.2434868249187417, 0.833830183278061, 2.19905955953892, 2.6778788113378678, 1.7645486768981606, 0.46763498389091124, -1.2180142110661276, -2.5986913120989277, -2.324327300397522, -1.5998343387142109, -0.1387680956279535, 0.988815035322009, 2.1752153602474844, 2.516768270408531, 1.9625512591966685, 0.408186761757472, -1.0678639027494354, -2.43645721505901, -2.6777946028639796, -1.5023654591078517, -0.20578808735821266, 1.1771493327144862, 2.1048105793305254, 2.3598470285419015, 1.725560436548979, 0.5370718282385052, -1.2072201432928433, -2.5887027126406656, -2.574042027709449, -1.6144949492632945, -0.1468233840694179, 1.0800016563556052, 2.0624388593497454, 2.5557569800161692, 1.7540766268817853, 0.6069920281353236, -1.0709249067752746, -2.4902667157996206, -2.448379078753832, -1.6188448008638818, -0.1943495804335362, 1.091762481005319, 2.007822879297535, 2.6002234741683665, 1.9340349869312703, 0.5307886784501193, -0.9670118759034269, -2.549876067058509, -2.6254349853821193, -1.524759133438829, -0.44100235245727804, 1.0495524044860007, 2.271397758857056, 2.5771846703870334, 2.0426224367348427, 0.473273705442812, -1.379925244800475, -2.4905889284402263, -2.44499584706523, -1.647038284815346, -0.2172265937728423, 1.1634552098787807, 2.183431941445094, 2.29588643299665, 1.778081789865725, 0.49695633846122284, -0.9868278492564672, -2.5044440726875883, -2.448379078753832, -1.6360831021977342, -0.4674236701520314, 0.997192601339873, 2.010722841740518, 2.697212106903642, 1.9251740007335878, 0.51806127336854, -0.7698187642481353, -2.6036856121136114, -2.6033633992036758, -1.5987065994665373, -0.2823132969732417, 0.9134169713248692, 2.129299190238984, 2.4341187356827514, 1.9921953060169082, 0.5391662115668647, -0.8511770367978757, -2.393280743829381, -2.5149159849519314, -1.7024586261541628, -0.2972961250001333, 1.0527745471021004, 2.0394002547439074, 2.6988232151689, 1.9250128919039406, 0.5034005930484444, -0.7848015753455219, -2.5561592164090015, -2.540209684012763, -1.5170260659071562, -0.2111045763181546, 1.0070201315748044, 2.098849537253295, 2.494051720149844, 1.6504839639290882, 0.5201556564006945, -1.0902575638454186, -2.4404848716032346, -2.4748005099165615, -1.6148171604910846, -0.2140044793410315, 1.206954195164503, 2.2032484062682065, 2.635023363172236, 1.916151906839288, 0.5702597525613128, -0.9228689755371423, -2.348815435665306, -2.326582786381139, -1.8397206799790513, -0.292301849078198, 0.9008506325183976, 2.0104006236852427, 2.7901731304368385, 2.0182949664757825, 0.6251970633448433, -0.9789336810184466, -2.4960665434437352, -2.5226490899023446, -1.7035863657611854, -0.02599402753919747, 1.1333281465541805, 2.253031259490961, 2.4755240437804695, 1.626156624701448, 0.6211694004631911, -1.1128123306028856, -2.4301740710720448, -2.638484611104082, -1.4984989255314265, -0.4767677942574449, 1.0084700951316639, 2.1810152998084513, 2.6435622280738515, 1.797414812671268, 0.5990978101346832, -1.054814359296358, -2.504121860015056, -2.5798418589166987, -1.9595833794384427, -0.2734524843274919, 0.9432217551498665, 2.0371447274412198, 2.5533403237042487, 1.817714492071268, 0.34374427188727685, -1.0754358600812206, -2.4356516837635254, -2.784447184770876, -1.5245980278637588, -0.5192996666956807, 0.8571906717843037, 1.9738288842110632, 2.5602680720674456, 1.876196933369387, 0.6195583353463663, -1.0490145622174363, -2.4303351773247486, -2.5141104532111873, -1.6974643508022735, -0.2210931310383625, 1.0257085523272367, 1.8911800457967867, 2.4956628227168123, 1.9085797932087176, 0.7970978387484952, -0.9910165915833513, -2.226374796500784, -2.402302692004093, -1.5597190447747507, -0.2492866302220141, 1.101106698851229, 2.0593777]

        self.fit_list = []

        self.datasets = {
            "Prom 1.5% PEO": self.fit_list,
        }

        self.colors = {
            "Prom 1.5% PEO": "black",
        }


        print(len(self.data))

    def sine_model(self, t, A, f, phi, C):
        return A * np.sin(2 * np.pi * f * t + phi) + C

    '''def measure():
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
            task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
            task.start()
            print("Running task. Press Ctrl+C to stop.")

            try:
                total_read = 0
                total_data = []
                while True:
                    data = task.read(number_of_samples_per_channel=1000)
                    read = len(data)
                    total_data += (data)
                    total_read += read
                    print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
            except KeyboardInterrupt:
                pass
            finally:
                task.stop()
                print(total_data)
                print("")
                print("")
                print(len(total_data))
                print(len(data))
                print(f"\nAcquired {total_read} total samples.")

                # Create an array of time points corresponding to the data (assuming uniform sampling)
                t = np.arange(len(data))

                # Fit the sine model to the data
                params, covariance = curve_fit(sine_model, t, data, p0=[np.max(data)-np.min(data), 0.1, 0, np.mean(data)])

                # Extract the fitted parameters
                A_fit, f_fit, phi_fit, C_fit = params

                # Generate the fitted sine wave using the fitted parameters
                fitted_data = sine_model(t, A_fit, f_fit, phi_fit, C_fit)

                # Plot the original data and the fitted sine wave
                plt.figure(figsize=(10, 6))
                plt.plot(t, data, label='Original Data', marker='o', markersize=4)
                plt.plot(t, fitted_data, label='Fitted Sine Wave', linestyle='-', color='r')
                plt.legend()
                plt.xlabel('Sample Index')
                plt.ylabel('Voltage')
                plt.title('Sine Wave Fit to Data')
                plt.show()

                # Print the fitted parameters
                print(f"Amplitude (A): {A_fit}")
                print(f"Frequency (f): {f_fit} Hz")
                print(f"Phase (phi): {phi_fit} radians")
                print(f"Vertical offset (C): {C_fit}")

    '''


    def fit_sec(self, data_input):
        # Data van de fotodetector
        self.data = np.array(data_input)  # Vul hier de fotodetectordata in
        self.sampling_rate = 1e3  # Voorbeeld sampling rate in Hz (pas aan naar jouw systeem)

        # Bereken de FFT
        self.n = len(self.data)
        print ("n= ", self.n)
        self.fft_result = fft(self.data)
        self.frequencies = fftfreq(self.n, d=1/self.sampling_rate)  # Frequenties bij FFT

        # Behoud alleen de positieve frequenties
        self.positive_frequencies = self.frequencies[:self.n // 2]
        self.positive_fft = np.abs(self.fft_result[:self.n // 2])

        # Vind de dominante frequentie
        self.dominant_frequency_index = np.argmax(self.positive_fft)
        self.dominant_frequency = self.positive_frequencies[self.dominant_frequency_index]

        # Visualiseer de frequentiespectrum
        plt.figure(figsize=(10, 6))
        plt.plot(self.positive_frequencies, self.positive_fft)
        plt.title("FFT van de fotodetectordata")
        plt.xlabel("Frequentie (Hz)")
        plt.ylabel("Amplitude")
        plt.grid()
        plt.show()

        # Snelheid berekening
        self.wavelength = 632.8e-9  # Voorbeeld golflengte in meters (532 nm voor groen licht)
        self.theta = np.radians(4.5)  # Voorbeeld hoek tussen de bundels in graden
        self.velocity = (self.wavelength / 2) * self.dominant_frequency / np.sin(self.theta)

        print(f"Dominante frequentie: {self.dominant_frequency:.2f} Hz")
        print(f"Geschatte snelheid: {self.velocity:.2f} m/s")


    def snelheid_functie(self, x, a, b, x0):
        return a * (x - x0) ** 2 + b

    def process_and_fit_shifted(self, dataset, label, color):
        self.metingen = dataset[0]
        self.r = dataset[1]

        # Fit the model
        self.model = models.Model(self.snelheid_functie)
        self.result = self.model.fit(self.metingen, x=self.r, a=0, b=np.mean(self.metingen), x0=0)

        # Extract fitting parameters
        self.a = self.result.params['a'].value
        self.b = self.result.params['b'].value
        self.x0 = self.result.params['x0'].value

        # Calculate the shift to align the peak (x0) to zero
        self.shift = -self.x0
        self.r_shifted = [self.val + self.shift for val in self.r]

        # Generate the shifted fit
        self.r_fine_shifted = np.linspace(min(self.r_shifted), max(self.r_shifted), 200)
        self.y_fit_shifted = self.snelheid_functie(self.r_fine_shifted, self.a, self.b, 0)  # x0 is zero after shifting

        # Plot shifted data and fit
        plt.plot(self.r_shifted, self.metingen, 'o', label=f"{self.label} Data (Shifted)", color=self.color, alpha=0.6)
        plt.plot(self.r_fine_shifted, self.y_fit_shifted, '-', label=f"{self.label} Fit (Shifted)", color=self.color)

        # Main execution for shifting and plotting
    plt.figure(figsize=(12, 8))
    for label, dataset in datasets.items():
            process_and_fit_shifted(dataset, label, colors[label])

    plt.xlabel('r (shifted)')
    plt.ylabel('metingen')
    plt.title('Quadratic Fits with Peaks Aligned at r=0')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid()
    plt.tight_layout()
    plt.show()


    process_and_fit_shifted(self.fit_list)






