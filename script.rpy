# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Pak_Surya = Character("Pak Surya", color= "#c00ec0")
define Alex = Character("Alex", color= "#eadb0e")
define Bobby = Character("Bobby", color= "#EE2C2C")
define Syanin = Character("Syanin", color="#0e12f9")

image example = Movie(play="images/cutscene.webm", size=(1920,1080),loop= True, xalign=0.10, yalign=0.10)

# The game starts here.

label start:
   scene credit1
   pause(2.0)
   scene credit2
   pause(2.0)
   scene credit3
   pause(2.0)
   scene disclaimer
   pause(2.0)
   with dissolve



label awal :
   show black
   play music "audio/bgm_awal.mp3" fadein 0.1 volume 0.75
#latar full black (monologue)
   with fade
   centered"Rezim pemerintah baru yang sebenarnya sudah tidak disukai 
   oleh kelompok mahasiswa dan akademisi dari awal"
   with dissolve
   centered"mulai berulah kembali dengan peraturan-peraturan yang tidak masuk akal dan memberatkan kelompok menengah kebawah"
   with dissolve
   centered"hanya menguntungkan kelompok atas"
   with fade

#latar kamar belajar bobby
label perkenalan :
   #perkenalan alex nanti di zoom in character alex

   scene kos bobby
   show alex base
   "Namaku Alex, Aku adalah mahasiswa semester 5 dari Universitas Guyub Rukun yang aktif dalam himpunan dan kegiatan kemasyarakatan"
   show alex base at left 
   Alex "Aku percaya bahwa himpunan mahasiswa akan menjadi media yang baik bagiku untuk mengaktualisasi diri yaitu mengabdi pada Masyarakat dan membela hak mereka"
   Alex "Aku percaya bahwa bangsa yang sukses adalah bangsa yang rakyatnya sejahtera di kalangan manapun, dan dapat berkolaborasi dalam berbagai kesuksesan"
   Alex "Dan, Aku percaya, bahwa Indonesia akan mencapai massa dimana semua itu terwujud, itulah mimpiku"
   Alex "Namun, rezim pemerintahan baru ini terlihat menghalangi proses terwujudnya mimpi itu, karena sungguh banyaknya kebijakan yang tidak menjunjung keadilan dan kesejahteraan bagi seluruh kelompok"
   Alex "Aku harus bertindak untuk menyelesaikan semua ini…"
   hide alex base
   with fade

   #perkenalan character bobby zoom in bobby alexnya ilangin

   show bobby base
   "Aku Bobby, sama seperti temanku Alex, aku merupakan mahasiswa semester 5 dari Universitas Guyub Rukun yang juga aktif dalam kegiatan kemahasiswaan dan kemasyarakatan"
   show bobby base at left
   Bobby "Aku disini mencari keadilan atas segala Tindakan egois pemerintah yang selama ini merajalela sesuka mereka"
   Bobby"Aku sangat ingin untuk berpengabdian dan berperan dalam Masyarakat, namun ini lebih dari sekedar itu"
   Bobby"Ada hal yang harus diluruskan, ada hal yang harus dikuak, ada hal yang harus dibuktikan, dan ada hal yang harus diberhentikan"
   Bobby"Munafik bagiku untuk berbicara bahwa ini bukan tentang sebuah dendam akan kisah pilu lama"
   Bobby"Sudah saatnya ini semua berubah!! Ayah… akan ku lanjutkan perjuanganmu itu…"
   hide bobby base
   with fade



label demo:
   scene bg demo
   play music"audio/bgm_demo.mp3" fadein 0.2
   #latar demo depan gedung DPR
   "Alex dan Bobby sangat frustasi dan akhirnya turun ke lapangan untuk berdemonstrasi. Pada demonstrasi ini, Alex, Bobby, dan juga Syanin menjadi orang yang menyuarakan protes dan aspirasi mereka kepada pihak pemerintahan."
   with fade
# kasih sfx keramaian orang demo sama music aga mencekam

   #latar kerusuhan kasih bg music chaos
   "Namun apa daya, ternyata banyak mahasiswa yang menjadi korban kekerasan dari pihak aparat kepolisian"
   "Dan bahkan pemerintah menanggapi demonstrasi ini dengan suatu kebijakan yang tampaknya meringankan namun detail mengenai kebijakannya ternyata semakin memberatkan kelompok menengah kebawah"
   with fade


   #latar demo depan gedung DPR
   scene gedung dpr
   "Bobby melihat ini sudah muak, dan akhirnya pada saat demonstrasi kedua, dia mendengar beberapa orang di sekitarnya mengeluhkan hal yang sama dan sudah sangat muak"
   "Mereka mulai merencanakan beberapa strategi untuk memuat jera pemerintah yaitu denga membentuk kelompok pemberontakan/radikalisme"
   "Pendemo" "Mau sampai kapan kayak gini, gaakan ada perubahan kalo begini caranya"
   "Pendemo" "Kita Cuma bakal dibungkam, dibungkam, dan dibungkam terus menerus sampai kita diam"
   
   show syanin_agreeing at left
   Syanin "Gua juga udah muak dengan semua ini, pemerintah pun gaakan ngapa-ngapain, mereka udah tutup telinga dan seenaknya sama kita semua"
   Syanin "Apapun yang penting mereka Sejahtera, kita? Mereka mana peduli sama kita, ibarat kata Cuma aspal yang mereka injak dan rusak selama perjalanan mereka"
   Syanin "Kita harus melakukan sesuatu, harus kita kasih pelajaran para orang-orang brengsek ini."
   hide syanin_agreeing

   "Pendemo" "Setuju! Ayo kita buat ledakan peringatan! Kita buat jera mereka"

   "Bobby mendengarnya namun dia berusaha tidak menghiraukan mereka dan ikut Alex untuk pulang"
   "Namun ditengah jalan ia berubah pikiran…"
   with fade

   scene bg_trotoar
   #latar trotoar lingkungan perkotaan music calm aja
   play music"audio/bgm_city.mp3"
   #show character bobby alex satu persatu tiap ngomong

   show bobby base at left
   Bobby "Eh lek, lu duluan aja deh, gua lupa ada meeting organisasi pengmas."
   hide bobby base
   Alex "Buset, tiba tiba amat. Yaudah gapapa nih gua tinggal?"
  
   show bobby base
   Bobby "Iya, aman aja, ntar gua kabarin klo ada apa-apa"
   hide bobby base
   with fade
   

   #latar di depan gedung tua ada segerombolan mahasiswa
   "Bobby berkata bahwa dia ada urusan, padahal sebenarnya dia mencari kelompok mahasiswa tadi dan memutuskan untuk bergabung dengan kelompok pemberontakan yang diketuai oleh Syanin"
   with fade
   
   
   scene black
#timeskip 1 bulan
   centered"Satu bulan kemudian..."
   with dissolve
   "Ada sebuah berita bahwa terdapat ledakan pada Gedung DPR. Alex dan Bobby melihat berita itu di TV saat mereka sedang belajar bersama"
   with fade
   "Melihat hal itu, mereka berdua sudah langsung memiliki pemikiran yang sama bahwa aksi ini merupakan aksi kontra pemerintah atas berbagai keputusan yang telah dibuat beberapa waktu lalu"

   play music "audio/bgm_kamar.mp3" fadein 0.1 volume 0.6
   #latar kamar belajar bobby lagu chill aja sfx burung atau apalah
   show kos bobby
   Alex "Weh, kenapa jadi gini. Siapa ya yang kira-kira berulah kayak gini? Ga gini sih caranya. Kalo ini dilakuin terus-terusan, Masyarakat sekitar yang malah kena imbasnya"
   with fade

   show bobby base at left
   Bobby "Gua sih setuju dengan Gerakan kyk gini. Emang harus dibikin jera pemerintah brengsek ini. Kalo Cuma demonstrasi-demonstrasi biasa, kita gaakan didengar, Cuma nyamuk dan lalat di telinga mereka"
   Bobby "Lu gatau sebetapa kotornya pemerintah ini diluar dari kebijakan-kebijakan bodoh mereka. Tanpa kita tau, banyak rahasia gelap dari tindakan mereka yang lebih parah dari gerakan peringatan kecil kayak gini"
   Bobby "Gaada apa-apanya lah dibanding ledakan kecil kayak gini, apalagi demonstrasi yang lama-lama mula gaada gunanya ini"
   hide bobby base
   with fade



   #latar demonstrasi di depan gedung DPR
   scene gedung dpr
   "Beberapa waktu kemudian, ada ajakan gerakan lanjutan untuk demonstrasi turun ke lapangan di depan gedung DPR untuk protes akan beberapa hal. Alex mengajak namun Bobby menolak dengan alasan sebut urusan organisasi kampus"
   with dissolve
   "Di saat demonstrasi terjadi, terdapat juga sebuah ledakan lanjutan dari yang pertama. Aparat, beberapa properti aset pemerintah, bahkan mahasiswa yang turun ke lapangan menjadi korban dari ledakan tersebut"
   with dissolve



   #latar gedung kos
   show gedung kos
   "Selesai demonstrasi, Alex kembali ke kos (kos mereka sama), dan berbenah benah siap siap belajar bersama Bobby di kamar Bobby, lalu saat di kamar Bobby, Bobby ingin memasak untuk makan malam"
   with fade
   

   #latar meja belajar dengan laptop menyala
   scene bg_laptop
   with fade
   "Alex melihat di laptop Bobby ada window yang sedikit aneh, ada peta gedung DPR yang diledakan tadi dengan beberapa catatan-catatan yang menjelaskan tentang step-by step suatu rencana. Alex curiga namun berusaha mengalihkan pikirannya dan meragukan asumsinya."
   with dissolve


   #latar tangan Bobby yang ada luka
   show tangan bobby
   with fade
   "Namun ketika Bobby kembali membawa makan malam, Alex melihat sebuah luka yang terlihat aneh. Alex takut namun dia harus bertanya tentang kecurigaan ini"
   with dissolve

   #latar Alex dan bobby di ruang belajar
   # awalnya bg musicnya santai trus kayk tegang gitu
   scene kos alex
   play music"audio/bgm_awal.mp3" fadein 0.6 volume 0.3
   Alex "Itu kenapa tangan lu Bob? Gapernah liat gua sebelumnya"

   show bobby base at left
   Bobby "Oh ini, iya luka bakar pas masak kemaren, biasalah bengong"
   hide bobby base
   
   Alex "Oh..."
   with fade

   Alex "Lu belakangan ini ada kegiatan apa sih Bob, kyknya lagi sibuk banget akhir-akhir ini…"
   
   show bobby base at left
   Bobby "Ya pengmas doang sih, gaada yang lain… paling kegiatan BP himpunan juga, itupun kecil-kecilan"
   hide bobby base
   
   Alex "Maaf banget Bob, gua ga bermaksud tapi ini random thoughts aja… kok di laptop lu ada denah DPR gitu? Gua tadi ga sengaja liat"
   show bobby base at left
   Bobby ".... Maksud lu, lu nuduh gua bagian dari gerakan kelompok berontak itu"
   hide bobby base
   with fade

   Alex "Engga, serius cuma penasaran doang"
   with fade

   show bobby base at left
   Bobby "Udahlah lex, gausah ngelak, gua udah tau ini arahnya kemana. Kalo lu udah curiga, ya disini gua jawab kecurigaan lu. Gua memang bagian dari kelompok itu, saat demonstrasi beberapa waktu lalu, gua denger ada kelompok mahasiswa yang pengen ngelakuin suatu gerakan pemberontakan melawan pemerintah"
   Bobby "Pas denger mereka, perasaan gua merasa terwakili dan insting gua berkata untuk ikut mereka. Mungkin lu gasuka lek, tapi maaf, ini jalan yang udah gua pilih"
   hide bobby base
   with fade

   Alex "Tapi kenapa Bob, sampe sejauh ini? Akal sehat lu dimana? Kita itu mahasiswa, kita itu orang berpendidikan, harusnya kita bijaksana dalam bertindak apalagi tentang hal kyk gini"

   show bobby base at left
   Bobby "Gini ya lek, lu tuh gatau apa aja tindakan gelap yang udah dilakukan pemerintahan selama ini. Lu mungkin heran, kenapa gua bisa tau? Ya karena dulu alm. bokap gua juga bagian dari pemerintahan itu"
   Bobby "Berbeda dengan para brengsek itu sekarang, bokap gua punya tujuan mulia untuk mewakili kelompok grassroot nya. Tapi, Ketika dia tahu beberapa rahasia gelap pemerintahan, dia langsung dibungkam dan keluarga gua disuruh tutup mulut sampai sekarang"
   Bobby "Lu pikir gua bisa diem aja? Lu pikir gampang buat bertindak dengan ‘akal sehat’ dengan pengalaman buruk, impresi lucu yang udah dibuat pemerintah ini? Haha, gamungkin"
   hide bobby
   with fade

   #latar Ruang kantor Pak surya (office pribadi)
   #lagu latar

   scene black
   play music"audio/bgm_kamar.mp3" fadein 0.6 volume 0.3
   centered "Pemerintah tentunya prihatin melihat peristiwa ledakan yang ada"
   with dissolve
   centered "Namun, Akal jahat Pak Surya sudah memiliki beberapa opsi untuk menyelesaikan masalah ini"
   with dissolve
   centered"Dia mengetahui bahwa Syanin dan Bobby merupakan salah dua dari kelompok tersebut"
   with dissolve
   
   scene bg_office
   with fade
   show pak surya_base 
   Pak_Surya "Hmm… sungguh unik cara mahasiswa-mahasiswa ini. Mereka sudah mulai berani buat melakukan hal-hal gila kayak gini"
   hide pak surya_base
   "Ajudan" "Betul pak, kami dapat info dari intel kita, bahwa kelompok tersebut diketuai oleh Syanin, seorang mahasiswa yang waktu itu pernah memimpin demonstrasi didepan Gedung DPR"
   "Ajudan" "Pada demonstrasi tersebut, ada 3 orang yang paling menonjol, ada seorang mahasiswa bernama Bobby yang merupakan anggota dari kelompok berontak itu, dan juga mahasiswa yang bernama Alex" 
   "Ajudan" "Alex ini sepertinya tidak ikut dalam kelompok tersebut Pak"
   "Ajudan" "Menurut saya, bapak bisa coba berbicara dengan salah satu dari 3 mahasiswa tersebut Pak, karena sepertinya mereka memiliki pengaruh besar dalam demonstrasi-demonstrasi ini."
   with dissolve

   show pak surya_agreeing at left 
   Pak_Surya "Info yang menarik, baiklah, akan coba saya pikirkan…"


   #latar pak surya dengan background thrilling (elemen warna merah dan tanda tanya)


scene black
label choices:
   centered"Dia memiliki opsi antara menjebak kelompok tersebut atau merekrut mereka sebagai orangnya"
   with dissolve
menu :
   "Pilih apa yang akan dilakukan Pak Surya"
   "Approach Syanin":
      jump pil1
   "Approach Bobby":
      jump pil2
   "Approach Alex " :
      jump pil3

label pil1 :
   scene bg_office
   with fade

   show syanin_base at left
   Syanin " Kalau cuma mau puji-puji, nggak perlu capek undang saya ke sini, Pak."

   show pak surya_base at right
   Pak_Surya "Langsung ke intinya, ya? Baiklah. Saya tahu kamu dan kelompokmu bergerak karena ingin perubahan. Saya paham kok, sistem kita memang nggak sempurna. Tapi kamu harus sadar, perubahan besar nggak bisa dicapai dengan cara yang kamu tempuh sekarang."

   Syanin "Dan cara yang Bapak tempuh lebih baik? Korupsi, manipulasi, tutup mata sama penderitaan rakyat?"

   Pak_Surya "Sistem ini ada bukan karena kebetulan, Syanin. Kalau kamu cerdas, kamu tahu bahwa semua ini soal pengendalian. Kamu bisa berteriak di jalan sekeras apa pun, tapi nggak akan ada yang benar-benar berubah kalau kamu nggak punya kekuasaan."

   Syanin "Jadi apa maksud Bapak bawa saya ke sini?"

   Pak_Surya "Saya ingin menawarkan kerja sama. Gabunglah dengan saya. Masuk tim saya. Kamu bisa punya pengaruh nyata untuk membuat perubahan yang kamu inginkan, tanpa perlu aksi nekat atau kekerasan. Dengan posisi di pemerintahan, kamu bisa bantu membangun sesuatu yang lebih baik dari dalam."

   Syanin "Masuk tim Bapak? Jadi bagian dari sistem yang saya lawan? Serius, Pak?"

   Pak_Surya "Saya serius. Ini kesempatan besar, Syanin. Dengan kemampuan kamu, kamu bisa jauh lebih berguna di sisi saya dibandingkan terus melawan tanpa hasil. Bayangkan apa yang bisa kita capai bersama."
   Pak_Surya "Syanin, saya sering dengar nama kamu akhir-akhir ini. Pemuda idealis yang berani menentang arus. Saya suka semangat kamu."

menu :
   "Pilih apa yang akan dilakukan oleh Syanin"
   "Berbicara dengan Pak Surya":
      jump pil1_1
   "Pergi dari tempat Pak Surya":
      jump pil1_2



label pil1_1:
   scene bg_office
   with fade

   show syanin_base at left
   show pak surya_base at right

   Syanin "Kalau saya setuju... apa yang Bapak inginkan dari saya, tepatnya?"

   Pak_Surya "Sederhana saja. Saya butuh kamu untuk membantu meredam ancaman dari kelompokmu sendiri. Kamu lebih dekat dengan mereka, lebih tahu cara berpikir mereka. Dengan bantuanmu, kita bisa mengakhiri kekacauan ini tanpa perlu banyak korban."

   Syanin "Meredam? Maksudnya menangkap mereka semua?"

   Pak_Surya "Bukan hanya menangkap, Syanin. Kita bicara soal menghentikan ide radikal sebelum mereka menyebar lebih jauh. Beberapa dari mereka mungkin masih bisa 'dibimbing'. Tapi mereka yang berbahaya... harus diisolasi."

   Syanin "Dan bagaimana dengan mereka yang cuma ikut-ikutan? Mahasiswa yang hanya ingin suara mereka didengar?"

   Pak_Surya "Itu pilihanmu, Syanin. Kalau kamu ingin melindungi mereka, saya bisa mempertimbangkannya. Tapi ingat, semakin banyak yang kita biarkan, semakin besar risiko yang kita tanggung."

   Syanin "Dan kalau saya nggak setuju dengan cara Bapak menangani ini?"

   Pak_Surya "Kamu sudah setuju untuk bergabung. Keputusan ini bukan lagi soal setuju atau tidak, Syanin. Ini soal bagaimana kamu akan menggunakan posisimu. Melindungi yang bisa dilindungi... atau menyerahkan mereka semua untuk kebaikan yang lebih besar."

   Syanin "...Saya perlu waktu untuk berpikir."

   Pak_Surya "Ambil waktu yang kamu butuhkan. Tapi ingat, waktu itu terbatas. Semakin lama kamu ragu, semakin banyak nyawa yang terancam. Ini kesempatanmu untuk menjadi pahlawan, Syanin. Jangan sia-siakan."

   Syanin "(Mengangguk pelan, lalu bangkit dan berjalan keluar tanpa menoleh lagi)"

   Pak_Surya "(Sambil melihat punggung Syanin pergi, berbicara sendiri dengan nada dingin) Kita lihat seberapa jauh idealismemu bisa bertahan..."

menu :
   "Pilih apa yang akan dilakukan syanin"
   "Bergabung dengan Pak Surya":
      jump pil1_1_1
   "Tolak tawaran Pak Surya":
      jump pil1_1_2


label pil1_1_1:
# Scene awal: Ruangan kantor Pak Surya
   scene bg_office with fade
   play music "audio/suspense_theme.mp3" fadein 1.0 volume 0.6
    
   # Pak Surya bicara, Syanin belum muncul
   show pak surya_base at right
   Pak_Surya "Operasi sudah dimulai. Mereka yang menyebabkan kerusuhan ini akan segera diamankan."
   Pak_Surya "Kamu sudah membuat keputusan yang tepat, Syanin."
   hide pak surya_base with dissolve

   # Syanin mulai bicara, munculkan karakter Syanin
   show syanin_base at left
   Syanin "Tapi Alex... dia nggak ada sangkut-pautnya sama semua ini."
   Syanin "Dia hanya ikut suara teman-temannya."
   hide syanin_base with dissolve

   # Pak Surya berbalik, munculkan Pak Surya kembali
   show pak surya_base at right
   Pak_Surya "(Berbalik, menatap Syanin dengan tajam) Radikalisme, Syanin, tidak memilih korban."
   Pak_Surya "Jika dia ada di barisan itu, maka dia bagian dari masalah."
   Pak_Surya "Jangan biarkan perasaanmu mengaburkan logika. Kita butuh stabilitas, bukan simpati."
   hide pak surya_base with dissolve

   # Reaksi Syanin yang ragu
   show syanin_base at left
   Syanin "(Menggertakkan gigi, suaranya bergetar) Tapi dia nggak bersalah, Pak."
   hide syanin_base with dissolve

   # Pak Surya kembali bicara dengan nada lebih tegas
   show pak surya_base at right
   Pak_Surya "(Nada suaranya tegas, penuh tekanan) Dan kamu sudah memilih untuk berada di sisi yang benar."
   Pak_Surya "Jangan ragu sekarang. Dunia ini tidak hitam putih, Syanin."
   Pak_Surya "Kadang, pengorbanan diperlukan demi tujuan yang lebih besar."
   hide pak surya_base with dissolve

   # Syanin terdiam, suasana tegang
   show syanin_base at left
   Syanin "(Terdiam, menunduk dengan perasaan berat.)"
   hide syanin_base with dissolve

   # Efek suara sirine dan suara pintu didobrak
   play sound "audio/sirine.mp3" volume 0.8
   "Dari luar terdengar bunyi sirine yang makin dekat, diikuti suara pintu didobrak dan teriakan mahasiswa."

   # Pak Surya melihat keluar jendela
   show pak surya_base at right
   Pak_Surya "(Pelan, seperti bicara sendiri) Ini baru permulaan."
   hide pak surya_base with dissolve

   # Reaksi terakhir Syanin
   show syanin_marah at left
   Syanin "(Menggenggam tangannya erat, matanya penuh dengan rasa bersalah, tetapi dia tetap membisu.)"
   hide syanin_marah with fade

   # Scene berakhir
   scene black with fade
   stop music fadeout 2.0   

return

label pil1_1_2:
   # Scene awal: Ruangan kantor Pak Surya
   scene bg_office with fade
   play music "audio/suspense_theme.mp3" fadein 1.0 volume 0.6
   
   # Pak Surya berbicara dengan nada tajam
   show pak surya_base at right
   Pak_Surya "(Menyilangkan tangan di depan dada, tatapannya tajam) Kamu benar-benar menolak tawaran saya, Syanin?"
   Pak_Surya "Ini bukan hanya soal idealisme. Ini soal bertahan hidup di dunia nyata."
   hide pak surya_base with dissolve
   # Syanin menjawab dengan tegas
   show syanin_base at left
   Syanin "(Nada tegas, tatapannya tidak goyah) Kalau dunia nyata seperti yang Bapak tawarkan, saya nggak mau ikut andil."
   Syanin "Saya lebih baik mati berdiri daripada hidup berlutut di bawah sistem kotor ini."
   hide syanin_base with dissolve
   # Pak Surya bereaksi dengan sinis
   show pak surya_base at right
   Pak_Surya "(Tersenyum tipis, nadanya berubah sinis) Kamu masih muda, Syanin. Terlalu naif untuk memahami bagaimana kekuasaan bekerja."
   Pak_Surya "Orang-orang yang kamu lindungi itu nggak akan menghargai pengorbananmu."
   Pak_Surya "Mereka hanya akan menghancurkanmu ketika semuanya gagal."
   hide pak surya_base with dissolve
   # Syanin mendekat dan menatap langsung
   show syanin_base at left
   Syanin "(Mendekatkan tubuh ke meja, menatap langsung ke mata Pak Surya) Kalau saya harus gagal, setidaknya saya gagal di jalan yang benar."
   Syanin "Dan saya janji, kebenaran akan menang. Pemerintahan ini nggak akan selamanya bisa sembunyi di balik topeng."
   hide syanin_base with dissolve
   # Pak Surya tertawa kecil
   show pak surya_base at right
   Pak_Surya "(Tertawa kecil, menggelengkan kepala) Kamu benar-benar keras kepala. Baiklah, Syanin."
   Pak_Surya "Kalau itu pilihanmu, jangan salahkan saya kalau ke depannya kamu akan menyesal."
   hide pak surya_base with dissolve
   # Syanin mundur dengan yakin
   show syanin_base at left
   Syanin "(Melangkah mundur, tersenyum kecil dengan nada penuh keyakinan) Saya nggak akan menyesal, Pak. Tapi saya yakin Bapak yang akan menyesal nanti."
   hide syanin_base with dissolve
   # Suara langkah kaki Syanin
   play sound "audio/footsteps.mp3" volume 0.6
   "Syanin berbalik dan meninggalkan ruangan, langkahnya tegas meski dadanya dipenuhi emosi."
   # Pak Surya mengambil telepon dengan ekspresi tajam
   show pak surya_base at right
   Pak_Surya "(Berbicara pelan tapi penuh tekanan) Awasi dia. Jangan biarkan dia keluar dari radar kita."
   hide pak surya_base with dissolve
   # Scene berakhir
   scene black with fade
   centered"END"
   stop music fadeout 2.0
   return


label pil1_2:
   # Scene awal: Ruang bawah tanah - markas rahasia
   scene bg_markas with fade
   play music "audio/tense_theme.mp3" fadein 1.0 volume 0.6
   "Ruangan ini suram, dengan dinding bata yang terkelupas dan lampu gantung berpendar lemah."
   "Suasana terasa berat, dengan campuran amarah dan ketidakpastian."
   # Syanin bicara
   show syanin_base at left
   Syanin "(Dengan nada tegas, tanpa basa-basi) Kita punya masalah. Pak Surya tahu terlalu banyak tentang kita. Dia coba rekrut aku buat jadi bagian dari timnya."
   hide syanin_base with dissolve
   # Bobby mendekat, marah
   show bobby base at right
   Bobby "(Mendekat, alisnya terangkat, nada marah) Apa?! Jadi dia tawarin kamu untuk jadi pengkhianat?"
   hide bobby base with dissolve
   # Syanin menjawab tajam
   show syanin_base at left
   Syanin "(Menatap Bobby dengan tajam) Aku tolak, jelas. Tapi dia nggak bakal diam. Dia pasti bergerak lebih cepat dari yang kita kira."
   hide syanin_base with dissolve
   # Anggota Kelompok 1 bicara (tidak menampilkan gambar)
   "Anggota Kelompok 1" "(Dengan suara gusar) Berarti kita harus lebih dulu gerak! Kalau kita diam, mereka yang bakal menangkap kita satu-satu!"
   # Bobby hentakkan tangan ke meja
   show bobby base at right
   Bobby "(Menghentakkan tangan ke meja, menatap peta) Kita nggak punya pilihan. Kalau mereka main keras, kita harus lebih keras. Aksi yang sebelumnya cuma gertakan, sekarang kita eksekusi penuh!"
   hide bobby base with dissolve
   # Syanin menenangkan
   show syanin_base at left
   Syanin "(Menggeleng, suaranya penuh tekanan) Kita butuh strategi, Bobby, bukan sekadar emosi. Kalau kita gegabah, kita justru memperkuat propaganda mereka. Kita bakal dicap sebagai teroris."
   hide syanin_base with dissolve
   # Bobby menjawab tegas
   show bobby base at right
   Bobby "(Menatap Syanin dengan tatapan tajam, nadanya ketus) Jadi kamu mau apa? Diam nunggu mereka nangkep kita?"
   hide bobby base with dissolve
   # Anggota Kelompok 2 menyela (tidak menampilkan gambar)
   "Anggota Kelompok 2" "(Menyela, nada setuju dengan Bobby) Bobby benar. Ini perang, Syanin. Kita nggak bisa terus main aman. Kalau mereka nggak takut, kita bakal habis!"
   # Bobby mempertegas
   show bobby base at right
   Bobby "(Menatap Syanin lagi, suaranya lebih tegas) Kita harus tunjukkan kalau kita nggak bisa dianggap remeh. Ini waktunya kita buat mereka tahu siapa kita sebenarnya."
   hide bobby base with dissolve
   # Syanin mulai kehilangan kendali
   show syanin_base at left
   Syanin "(Terdiam, menatap meja dengan wajah berat, mencoba mencari celah untuk menghentikan rencana ini.)"
   hide syanin_base with dissolve
   stop music fadeout 2.0
   jump kafe_alex_bobby

label kafe_alex_bobby:
   # Scene: Kafe sepi di pinggir kota
   scene bg_cafe with fade
   play music "audio/suspense_calm.mp3" fadein 1.0 volume 0.5
   "Malam mulai turun. Alex duduk di meja dekat jendela, menatap keluar dengan cemas."
   "Bobby duduk di hadapannya, terlihat gelisah, matanya melirik ke sekeliling seolah khawatir seseorang mengawasi mereka."
   # Dialog dimulai
   show alex base at left
   Alex "(Menatap Bobby dengan curiga, suara rendah penuh ketegangan) Lo makin lama makin sibuk, Bobby. Lo bilang kita harus siap buat aksi besar, tapi gue nggak tau apa-apa. Gue nggak nyaman dengan semua ini."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Menghindari tatapan Alex, nada suaranya gugup) Gue... gue cuma ngatur segala sesuatunya. Lo nggak perlu khawatir. Semua udah terkendali."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Memandang tajam, nada suara semakin keras) Jangan bohong, Bob. Gue mulai ngerasa ada yang nggak beres. Lo nggak punya waktu buat gue lagi, lo nggak cerita apa-apa. Jadi, lo kasih gue penjelasan sekarang juga!"
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Suara Bobby mulai meninggi, tapi dia tetap menghindar) Udah gue bilang, semuanya udah diatur. Gue nggak bisa kasih tau lo lebih jauh."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Memegang pergelangan tangannya, mencoba menahan amarah) Jadi lo pikir gue cuma bakal diam aja, lo ngumpet-ngumpet begini? Gue berhak tau, Bobby! Kalau nggak, gue bakal cari tau sendiri."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Mata Bobby mulai tajam, penuh ancaman, suaranya lebih dalam) Lo nggak ngerti, Alex. Kalau lo nekat cari tau lebih jauh, lo akan nyesel."
   hide bobby base with dissolve
   # Alex bergerak ke meja lain
   play sound "audio/chair_move.mp3" volume 0.6
   "Alex mengerutkan kening, merasakan ketegangan semakin membesar. Tanpa sepatah kata pun, dia berdiri dan pergi menuju meja lain di kafe."
   "Di meja itu, terlihat sebuah file yang terbuka—rencana aksi yang terselip di antara tumpukan kertas."
   stop music fadeout 2.0
   scene black with fade

menu :
   "Apa yang seharusnya Alex lakukan"
   "Alex memaksa untuk bertanya":
      jump pil1_2_1
   "Alex menyelidiki sendiri":
      jump pil1_2_2


label pil1_2_1:
   # Scene awal: Kafe, Alex memaksa Bobby berbicara
   scene bg_cafe with fade
   play music "audio/suspense_build.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Tatapan semakin tajam, suara penuh tekanan) Udah cukup, Bob! Lo nggak bisa terus-terusan ngehindar dari gue."
   Alex "Semua ini makin aneh, lo makin nggak punya waktu buat gue. Gue butuh penjelasan sekarang juga!"
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Menghela napas kasar, menatap Alex dengan marah, suaranya mulai meninggi) Lo nggak ngerti, Alex!"
   Bobby "Lo nggak tahu apa yang gue harus atur! Kalau gue kasih tau lo semuanya, lo bakal benci sama gue! Lo nggak bakal bisa balik lagi, lo nggak bakal ngerti kenapa semua ini harus terjadi!"
   hide bobby base with dissolve
   show alex base at left
   Alex "(Dengan suara yang penuh desakan, tidak sabar lagi) Gue nggak peduli, Bob! Kalau lo terus-terusan nyembunyiin ini dari gue, gue akan cari tau sendiri!"
   Alex "Gue nggak bisa cuma diem aja, semua ini udah makin besar dan lo nggak pernah cerita!"
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Berkata dengan suara keras dan marah, akhirnya menyerah) Oke! Lo mau tau? Lo siap? Gue nggak peduli lagi!"
   Bobby "Kita nggak cuma demo, kita mau hancurin pemerintah! Ini bukan cuma soal lo dan gue, Alex. Kita bakal serang pusat kekuasaan mereka, ngejatuhin semuanya!"
   Bobby "Semua yang lo lihat selama ini cuma permukaan, gue udah punya rencana besar, kita nggak akan berhenti sampai semuanya hancur!"
   hide bobby base with dissolve
   show alex base at left
   Alex "(Terdiam mendengar semua yang baru saja diungkapkan Bobby. Kepalanya seperti berputar, wajahnya terasa kosong.)"
   Alex "(Bergumam dalam hati, tidak bisa berkata-kata) Gue nggak tau harus gimana lagi... kalau gue melapor, semuanya bisa hancur."
   Alex "(Kalau gue diam, itu sama aja dengan jadi bagian dari ini...)"
   hide alex base with dissolve
   stop music fadeout 2.0

# Pilihan yang dapat diambil Alex
menu:
      "Melaporkan Bobby kepada pemerintahan":
         jump melaporkan_bobby
      "Membungkam Bobby (membunuhnya)":
         jump membungkam_bobby
      "Mengorbankan diri sendiri":
         jump mengorbankan_diri

label melaporkan_bobby:
   # Scene melaporkan Bobby
   scene bg_pemerintah with fade
   play music "audio/dark_theme.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Menunduk, suara berat dengan penyesalan yang dalam) Lo nggak ngerti, Bobby. Gue nggak punya pilihan."
   Alex "Lo terlalu jauh, dan gue nggak bisa ngebiarin semuanya hancur begitu aja. Gue nggak mau lebih banyak orang yang kena dampaknya."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Dengan suara marah dan penuh kebencian, menggertakkan gigi) Jadi ini yang lo pilih, Alex?"
   Bobby "Lo bener-bener melaporin gue ke mereka? Lo kira itu bakal bikin semuanya beres? Lo pikir lo bakal aman setelah ini?"
   hide bobby base with dissolve
   show alex base at left
   Alex "(Suara lembut, penuh penyesalan) Lo benar. Gue… gue udah terjebak dalam permainan mereka."
   Alex "Mereka bakal menang, Bob. Pemerintah korup ini tetap berkuasa, dan gue… gue nggak tahu lagi bagaimana keluar dari ini."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Dengan tatapan penuh kebencian, gemetar karena marah, tapi ada rasa kehilangan) Gue nggak akan lupa ini, Alex."
   Bobby "Lo mungkin ngerasa benar sekarang, tapi kita semua kalah. Mereka menang, dan kita… kita cuma jadi korban dari permainan kotor ini!"
   hide bobby base with dissolve
   stop music fadeout 2.0
   return

label membungkam_bobby:
   # Scene membungkam Bobby
   scene bg_gudang with fade
   play music "audio/intense_theme.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Dengan suara tercekat, berdiri dengan tangan yang masih gemetar setelah melukai Bobby) Kenapa gue harus sampai begini, Bob?"
   Alex "Gue nggak punya pilihan... Gue nggak bisa biarin lo terus jadi ancaman buat semuanya."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Dengan suara lemah, bercampur marah dan kesakitan, memandang Alex dengan tatapan penuh kekecewaan) Lo... lo... ngekhianatin gue, Alex."
   Bobby "Lo bener-bener ngerusak segalanya, kan? Semua yang kita lakukan, semua yang kita percaya, lo buang gitu aja. Lo... lo bisa hidup dengan ini?"
   hide bobby base with dissolve
   show alex base at left
   Alex "(Mata berkaca-kaca, menatap Bobby, suara penuh penyesalan) Gue nggak tahu... Gue nggak tahu lagi, Bob."
   Alex "Ini semua nggak benar... tapi gue nggak bisa biarin rencana lo hancurin lebih banyak orang."
   hide alex base with dissolve
   "Beberapa anggota kelompok pemberontakan masuk ke dalam dan melihat keadaan Bobby yang terluka parah."
   "Pemerintah segera mengepung lokasi dan menangkap semua orang yang terlibat."
   stop music fadeout 2.0
   return

label mengorbankan_diri:
   # Scene Alex mengorbankan diri
   scene bg_markas with fade
   play music "audio/sad_theme.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Dengan suara berat, penuh tekad) Kalau ini satu-satunya cara untuk menghentikan semua ini, gue akan ambil."
   Alex "Gue akan jadi kambing hitam... gue akan menyerahkan diri ke pihak pemerintahan. Ini semua salah gue."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Dengan mata penuh penyesalan, berusaha mendekati Alex, suara gemetar) Alex... jangan."
   Bobby "Lo nggak harus gini. Lo nggak bisa korbankan diri lo kayak gini! Semua yang kita lakukan… nggak boleh sia-sia."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Menunduk, menahan air mata) Lo harus melanjutkan hidup, Bob."
   Alex "Lo masih punya kesempatan untuk memperbaiki semuanya. Lo harus berhenti… berhenti jadi bagian dari kelompok ini."
   hide alex base with dissolve
   scene black
   pause(2.0)
   centered "Bobby akhirnya melaporkan kelompok pemberontakan, tetapi Alex tetap ditangkap oleh pemerintahan korup."
   centered"Meskipun mengorbankan dirinya, Alex gagal mengubah keadaan. Pemerintahan tetap berkuasa, dan kelompok pemberontakan hancur."
   stop music fadeout 2.0
   return

label pil1_2_2:
   # Scene: Kafe, malam mulai turun
   scene bg_cafe with fade
   play music "audio/suspense_build.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Menghela napas panjang, menatap Bobby dengan serius) Bob, lo makin lama makin jauh. Ada apa, sih? Kenapa gue merasa semuanya makin besar dan lo malah makin susah dihubungin?"
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Melirik ke sekeliling dengan waspada, bicara pelan) Lo nggak ngerti, Alex. Semua ini nggak sesederhana yang lo pikirkan."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Dengan nada tegas, mencoba mencari penjelasan) Tapi gue udah mulai curiga. Lo nggak mau kasih tau rencana lo sama gue? Lo nggak bisa terus-terusan begini, Bob. Gue butuh tahu apa yang lo lakuin."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Terlihat ragu, matanya gelisah, namun tetap menjaga jarak) Lo nggak perlu tahu, Alex. Ini bukan tempatnya buat ngobrol soal itu."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Mencoba mendesak, berdiri dari kursinya) Kalau lo nggak mau cerita, gue bakal cari tahu sendiri. Gue harus tahu apa yang sebenernya lo lakuin dan siapa yang terlibat di sini."
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Tegang, hampir berbisik) Alex, lo nggak ngerti apa yang lo hadapi. Lo pikir ini cuma soal demo, soal aksi. Tapi ini jauh lebih besar dari itu. Dan kalau lo nyentuh itu, lo bakal jadi target juga."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Menatap Bobby tajam) Kenapa lo nggak bisa percaya sama gue? Apa lo nggak tahu gue di sini cuma buat bantu lo?"
   hide alex base with dissolve
   show bobby base at right
   Bobby "(Berbicara pelan, seperti memutuskan sesuatu) Lo nggak ngerti, Alex. Gue cuma bisa kasih tahu lo satu hal, jangan ikut campur. Ini bukan urusan lo."
   hide bobby base with dissolve
   show alex base at left
   Alex "(Mengambil keputusan cepat, berjalan menuju meja yang berisi file berkas) Lo nggak mau cerita? Gue bakal cari tahu sendiri."
   hide alex base with dissolve
   centered "Bobby tampak makin cemas, merasa terpojok oleh keputusan Alex yang semakin keras kepala."
   stop music fadeout 2.0

# Pilihan yang bisa dipilih oleh Alex
menu:
      "Mengorbankan pihak keluarga":
            jump mengorbankan_keluarga
      "Mengorbankan pemerintahan":
            jump mengorbankan_pemerintahan
   

label mengorbankan_keluarga:
   # Scene: Percakapan dengan pihak pemberontakan
   scene bg_pemerintah with fade
   play music "audio/suspense_build.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "(Dengan suara tercekat, penuh penyesalan) Apa lo bener-bener mau gue pilih antara mereka? Apa lo nggak punya hati?"
   hide alex base with dissolve
   
   "Telepon (Suara anggota kelompok pemberontakan)" "(Suara dingin dan penuh ancaman) Lo dengar, kan? Kalau lo coba cabut bom itu, keluarga lo bakal dibunuh, Alex. Kami tahu di mana mereka tinggal. Lo pilih, hidup mereka atau hidup para pejabat pemerintahan."
   
   show alex base at left
   Alex "(Menutup mata sejenak, napasnya berat, lalu berbicara dengan tekad) Lo menang. Gue akan pilih untuk selamatkan pemerintahan. Tapi lo harus janji keluarga gue selamat."
   hide alex base with dissolve
   
   "Telepon (Suara anggota kelompok pemberontakan)" "(Tertawa kecil, seolah puas dengan keputusan Alex) Bagus. Lo bakal lihat betapa kuatnya kita semua. Pemerintahan itu akan hancur, Alex. Lo nggak akan pernah bisa mengubahnya. Tapi buat sekarang, keluarga lo akan aman."
   
   show alex base at left
   Alex "(Dengan mata yang mulai berkaca-kaca, suara menahan emosi) Ini keputusan yang berat... tapi ini demi mereka."
   hide alex base with dissolve
   "Telepon (Suara anggota kelompok pemberontakan)" "(Dengan nada penuh ancaman, suara itu mulai terdengar puas) Jangan khawatir, Alex. Kalau lo buat keputusan yang tepat, semuanya akan berjalan lancar. Kita punya kekuasaan." 
   scene black
   centered "(Alex mengakhiri percakapan dan menatap layar ponselnya dengan perasaan hampa. Keputusan yang ia buat akan mengubah hidupnya selamanya.)"
   stop music fadeout 2.0
   return

label mengorbankan_pemerintahan:
   # Scene: Ruangan gelap dengan cahaya layar ponsel Alex
   scene bg_ruang_gelap with fade
   play music "audio/tense_suspense.mp3" fadein 1.0 volume 0.7
   show alex base at center
   Alex "(Menghela napas panjang, menatap layar ponselnya dengan cemas) Lo tahu apa yang harus lo pilih, Alex. Kalau lo pilih untuk cabut bom itu, lo selamatkan keluarga lo, tapi pemerintah tetap berjalan dan korup."
   Alex "(Tertunduk, napasnya berat, dia berpikir sejenak) Tapi kalau lo pilih untuk bunuh mereka semua... lo harus siap hadapi konsekuensinya."
   hide alex base with dissolve
   "Telepon (Suara anggota kelompok pemberontakan)" "(Suara dingin, penuh ancaman) Lo tahu apa yang harus lo pilih, Alex. Kalau lo pilih untuk cabut bom itu, lo selamatkan keluarga lo, tapi pemerintah tetap berjalan dan korup."
   "Telepon (Suara anggota kelompok pemberontakan)" "(Tapi kalau lo pilih untuk bunuh mereka semua... lo harus siap hadapi konsekuensinya.)"
   show alex base at center
   Alex "(Suara bergetar, berat dengan penyesalan) Lo bener-bener nggak kasih pilihan lain, ya? Kalau gue pilih untuk bunuh mereka... apa yang terjadi?"
   hide alex base with dissolve
   "Telepon (Suara anggota kelompok pemberontakan)" "(Suara tajam, penuh ketegasan) Pemerintahan itu bakal hancur. Ketidakstabilan yang kita ciptakan bakal jadi ledakan besar."
   "Telepon (Suara anggota kelompok pemberontakan)" "(Polisi, tentara, semuanya akan goyah. Kami bisa ambil alih, dan negara ini bakal berada di tangan kami.)"
   show alex base at center
   Alex "(Menatap layar ponselnya, berpikir sejenak) Tapi... lo tahu konsekuensinya? Setelah ini nggak ada jalan balik."
   Alex "(Pencarian terhadap kelompok pemberontakan bakal lebih ketat dari sebelumnya. Mereka akan mengejar kita tanpa ampun. Kita harus menghilang dari publik selamanya.)"
   hide alex base with dissolve
   "Telepon (Suara anggota kelompok pemberontakan)" "(Tertawa dingin) Kami sudah siap dengan itu, Alex."
   "Telepon (Suara anggota kelompok pemberontakan)" "(Semua orang yang melawan akan hilang dalam bayang-bayang. Yang kita perlukan hanya waktu. Kita akan melarikan diri, dan pemerintahan itu akan jatuh.)"
   show alex base at center
   Alex "(Menarik napas panjang, suaranya penuh keteguhan) Baik. Gue akan melakukannya."
   Alex "(Pemerintah itu harus runtuh. Gue akan lakukan apa yang perlu untuk menghancurkannya, dan kalau itu artinya hidup kami harus menghilang, ya sudah.)"
   hide alex base with dissolve
   "Telepon (Suara anggota kelompok pemberontakan)" "(Dengan penuh rasa puas) Bagus, Alex. Ini keputusan yang benar. Setelah ini, nggak ada jalan kembali. Kita akan mengguncang dunia ini."
   
   show alex base at center
   Alex "(Menghela napas, wajahnya penuh penyesalan, tetapi ada keteguhan di matanya) Kita lihat saja nanti. Selamat tinggal."
   hide alex base with dissolve
   stop music fadeout 2.0
   # Narasi setelah percakapan
   centered"Keputusan Alex untuk mengorbankan pemerintahan berarti mengorbankan masa depan yang ia kenal."
   centered"Ketidakstabilan akan melanda, dan pencarian ketat terhadap kelompok pemberontakan akan dimulai."
   centered"Mereka yang memilih untuk bertahan di luar jangkauan publik akan hilang, diselimuti dalam bayang-bayang yang gelap."
   centered"Alex tahu, keputusan ini akan menghancurkan banyak hal, tetapi di sisi lain, mungkin ini adalah satu-satunya jalan menuju keadilan yang selama ini dia perjuangkan."
   scene black
   centered"END"
   return




label pil2 :
   # Scene: Kantor Pak Surya
   scene bg_office with fade
   play music "audio/suspense_theme.mp3" fadein 1.0 volume 0.7
   show pak surya_base at right
   Pak_Surya "Bobby, gimana kalau kamu bekerjasama dengan saya?"
   hide pak surya_base with dissolve
   show bobby base at left
   Bobby "Bekerjasama gimana pak?"
   hide bobby base with dissolve
   show pak surya_base at right
   Pak_Surya "Saya punya penawaran, saya akan memberi kamu jabatan di pemerintahan dan menjadi timses saya."
   Pak_Surya "Saya juga akan membiayai kehidupan keluarga kamu sampai kamu sukses. Tapi kamu harus bergabung dengan saya dan melaporkan kelompok pemberontakan di gedung X."
   hide pak surya_base with dissolve

# Pilihan yang diambil oleh Bobby
menu:
      "Bobby menerima tawaran Pak Surya":
            jump menerima_tawaran
      "Bobby menolak tawaran Pak Surya":
            jump menolak_tawaran

label menerima_tawaran:
   # Scene: Kostan Bobby
   scene kos bobby with fade
   play music "audio/tense_theme.mp3" fadein 1.0 volume 0.7
   show bobby base at left
   Bobby "Tawaran yang bagus pak, saya mau menerimanya. Dan saya akan menjebak seluruh kelompok radikal tersebut."
   hide bobby base with dissolve
   show pak surya_base at right
   Pak_Surya "Oke bagus, laksanakan!"
   hide pak surya_base with dissolve
   # Scene: Kostan Bobby, diskusi dengan Alex
   show alex base at left
   Alex "Bobby, lu tega ya ngehianatin kita semua."
   hide alex base with dissolve
   show bobby base at right
   Bobby "Maafin gua Lex, gua terpaksa ngelakuin semua ini."
   hide bobby base with dissolve
   # Ditangkap oleh polisi
   scene bg_police_raid with fade
   play music "audio/suspense_raid.mp3" fadein 1.0 volume 0.8
   "Mereka pun ditangkap dan ditahan oleh polisi."
   stop music fadeout 2.0
   return

label menolak_tawaran:
   # Scene: Bobby menolak tawaran Pak Surya
   scene kos bobby with fade
   play music "audio/sad_theme.mp3" fadein 1.0 volume 0.7
   show bobby base at left
   Bobby "Maaf Pak Surya, saya tidak bisa menerima tawaran bapak."
   hide bobby base with dissolve
   # Scene: Bobby dibunuh oleh orang suruhan Pak Surya
   scene kos bobby with fade
   show pak surya_base at right
   Pak_Surya "(Suara sinis) Kalau begitu, biarkan orang saya menyelesaikan urusan ini."
   hide pak surya_base with dissolve
   show bobby base at left
   "Beberapa hari kemudian Bobby meninggal tertembak di dalam kostannya oleh orang suruhan Pak Surya."
   hide bobby base with dissolve
   # Scene: Reaksi masyarakat terhadap kematian Bobby
   scene bg_demo with fade
   play music "audio/chaos_demo.mp3" fadein 1.0 volume 0.8
   centered"Berita ini pun ramai di berbagai macam sosial media."
   centered"Masyarakat pun menuntut keadilan untuk Bobby dengan demonstrasi dan protes besar-besaran."
   centered"Pemerintahan pun akhirnya tidak punya pilihan untuk turun jabatan."
   stop music fadeout 2.0
   return

label pil3 :
   # Scene: Kantor Pak Surya
   scene bg_office with fade
   play music "audio/suspense_theme.mp3" fadein 1.0 volume 0.7
   show pak surya_base at right
   Pak_Surya "Alex, gimana kalau kamu bekerjasama dengan saya?"
   hide pak surya_base with dissolve
   show alex base at left
   Alex "Bekerjasama gimana pak?"
   hide alex base with dissolve
   show pak surya_base at right
   Pak_Surya "Saya punya penawaran, saya akan memberi kamu jabatan di pemerintahan dan menjadi timses saya."
   Pak_Surya "Saya juga akan membiayai kehidupan keluarga kamu sampai kamu sukses. Tapi kamu harus bergabung dengan saya dan membantu saya untuk membujuk Bobby dan kelompok pemberontakan di gedung X untuk mengobrol dengan saya."
   hide pak surya_base with dissolve

# Pilihan yang diambil oleh Alex
menu:
      "Alex menerima tawaran Pak Surya":
         jump Alex_menerima_tawaran
      "Alex menolak tawaran Pak Surya":
         jump Alex_menolak_tawaran

label Alex_menerima_tawaran:
   # Scene: Kostan Alex
   scene kos alex with fade
   play music "audio/tense_theme.mp3" fadein 1.0 volume 0.7
   show alex base at left
   Alex "Saya tertarik pak dengan penawarannya. Saya akan mencoba membujuk mereka semua."
   hide alex base with dissolve
   # Scene: Alex dan Bobby berbicara
   show bobby base at right
   Alex "Bobby, Pak Surya ngajakin kita semua sama kelompok demonstrasi waktu itu buat ngobrol-ngobrol di kantornya gimana mau gak? Kayaknya dia punya penawaran yang bagus."
   Bobby "Wah, boleh sih nanti aku coba kumpulin anak-anak yang lain buat ikut."
   hide bobby base with dissolve
   # Scene: Mereka berkumpul di kantor Pak Surya
   scene bg_office with fade
   centered"Akhirnya mereka pun berkumpul ke kantor Pak Surya."
   centered"Namun, mereka pun dijebak dan ditangkap semua."
   stop music fadeout 2.0
   return

label Alex_menolak_tawaran:
   # Scene: Alex menolak tawaran Pak Surya
   scene bg_office with fade
   play music "audio/sad_theme.mp3" fadein 1.0 volume 0.6
   show alex base at left
   Alex "Maaf Pak Surya, saya tidak bisa menerima tawaran bapak."
   hide alex base with dissolve
   # Scene: Demonstrasi terus berjalan
   scene bg_demo with fade
   play music "audio/chaos_demo.mp3" fadein 1.0 volume 0.8
   centered"Demonstrasi pun terus berjalan dengan rusuh dan tidak ada jalan keluar dan titik terang."
   stop music fadeout 2.0
   return




return