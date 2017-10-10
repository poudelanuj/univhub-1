import sys
import django
from django.db import transaction

django.setup()

from university.models import *;

true = True
none = None
null = None
false = False
university = {
    "name": "La Trobe University",
    "admission_requirements": {
        "topic": "Admissions",
        "description": "The easiest way to apply to study with us is to\u00a0apply online. Simply register on the \u2018Student Portal\u2019, log in with the identifications you will receive via email, complete the application form and submit the required academic transcripts. The list of items you need to scan and upload is as follows:\n\nCopies of all academic transcripts.\nProof of English language proficiency.\nAny other supplementary information or document specified in course-specific entry requirements.\n\nYou may also apply by sending the completed form and documents by post to the La Trobe campus where you wish to study.\nEnglish Language Requirements:\nIf you are applying for an undergraduate degree, you will need to have a minimum IELTS score of 6.0 or a score of 213 on the computer-based TOEFL. If you are applying for a postgraduate degree, you will need a minimum IELTS score of 6.5 with no individual band less than 6.0. Alternatively, you need to have scored at least 233 with a score of 5 in essay writing on the computer-based TOEFL.\nScholarships:\n\u00a0A select number of scholarships are available to the International students. Visit the La Trobe website for details."
    },
    "world_ranking": 351,
    "university_logo": "https://images1.content-hci.com/hca-cont/img/default/img_px.gif",
    "highlights": [
        "High quality, industry-related education.",
        "Affordably priced programs taught by academic experts.",
        "Ranked in the top 400 universities in the world.",
        "Culturally diverse student body."
    ],
    "university_url": "http://www.latrobe.edu.au/",
    "motto": "Study at a young, modern, culturally diverse university in vibrant Melbourne.",
    "detailed_desc": [
        {
            "topic": "About La Trobe",
            "description": "La Trobe is a young, culturally diverse and vibrant institution. Ranked in the top 400 universities in the world, La Trobe is consistently ranked among the best universities in Australia. Offering high quality, industry related education, La Trobe graduates include medical researchers, journalists, CEOs, politicians and athletes.\nThe University has seven campuses in locations across Melbourne, regional Victoria and Sydney. The main campus in Melbourne is surrounded by natural parklands and is a short distance to the city. You can easily explore all the fascinating sights and attractions the city has to offer.\nLa Trobe comprises of two colleges: the College of Arts, Social Sciences and Commerce and the College of Science, Health and Engineering. \u00a0Choose from a variety of programs, ranging from university pathways to undergraduate, postgraduate and research degree programs.\nCRICOS Provider Code: 00115M\nWhy Study at La Trobe?\nYoung- In 2017 La Trobe celebrates its 50th birthday.\nModern- $500 million + invested into world-class centres for learning and research.\nCulturally diverse- Ranked one of the top 200 most international universities in the world.\nVibrant- A wide variety of courses at campuses located across Melbourne, regional Victoria and Sydney."
        },
        {
            "topic": "Campuses",
            "description": "La Trobe has seven campuses\u00a0- Melbourne, City, Albury-Wodonga, Bendigo, Mildura, Shepparton and Sydney.\nMelbourne \nThe largest campus is spread over beautiful parkland and waterways. The campus offers student accommodation facilities, cafes and restaurants, library, fitness centre and a wildlife sanctuary. Close to public transport and with car parking available, it is only 14 kilometres from the city.\nCity\nLocated in Collins Street in the heart of Melbourne, the city campus offers courses in business, law and health and is home to the La Trobe Business School. Enjoy modern facilities close to shops, cafes and public transport.\nAlbury-Wodonga\nAlbury-Wodonga offers unique courses in modern facilities. Located along the Murray River, it is close to the home to the Murray-Darling Freshwater Research Centre.\nBendigo\nBendigo is La Trobe\u2019s second largest campus with over 5,000 local and international students. Bendigo is a 2-hour drive from Melbourne & close to National Parks and other attractions. The campus is home to the La Trobe Rural Health School and the Centre for Sustainable Regional Communities.\nMildura\nMildura is a small campus, with big benefits. Located along the Murray River, Mildura enjoys a warm climate, lower costs of living and is close to natural attractions including Mungo National Park and Perry Sandhills.\nShepparton\nLocated in the town centre, the campus has a new building providing modern teaching, study and communal meeting spaces. There is also a clinical learning unit offering the most advanced teaching technologies. The campus is close to the Goulburn River and students enjoy an affordable and relaxed lifestyle in a tranquil setting.\nSydney\nThe new campus is located on Elizabeth Street in the heart of the city centre. The campus is close to Chinatown, Hyde Park, cafes, shopping centres, accommodation and famous attractions including Darling Harbour and the Sydney Opera House."
        },
        {
            "topic": "Study Options",
            "description": "Choose from their excellent selection of programs. The College of Arts, Social Sciences and Commerce offers courses in key areas of business, marketing, humanities and social sciences, law and education. The College of Science, Health and Engineering offers a wide variety of courses in areas including allied health and molecular sciences, engineering, mathematics and statistics, public health, psychology, nursing and rural health.\nThe\u00a0College of Arts, Social Sciences and Commerce\u00a0comprises four schools:\n\nLa Trobe Business School\nSchool of Education\nSchool of Humanities and Social Sciences\nLa Trobe Law School\n\nThe\u00a0College of Science, Health and Engineering\u00a0comprises nine schools:\n\nSchool of Allied Health\nSchool of Cancer Medicine\nSchool of Engineering and Mathematical Sciences\nSchool of Life Sciences\nSchool of Molecular Sciences\nSchool of Nursing and Midwifery\u00a0\nSchool of Psychology and Public Health\nLa Trobe School of Rural Health\nSchool of Applied System Biology\n\nSubject Rankings\nLa Trobe\u2019s Life Sciences are ranked in the top 200 in the world (ARWU 2016) and includes:\n\nBiology & Biochemistry\nMolecular Biology & Genetics\nMicrobiology\nImmunology\nNeuroscience\nAgricultural Sciences\nPlant & Animal Science and Ecology/ Environment\n\nLa Trobe is rated \u201cwell above world standard\u201d for 19 fields of research (Excellence in Research for Australia Report 2015) including:\n\nAgricultural and veterinary sciences\nBiological sciences\nNursing\nPhysical Sciences\nPhysiology and Nutrition and Dietetics\n\nPopular Programs:\nThe Bachelor of Business is the most flexible business degree, and gives you the option to experience different subjects before you decide on a major. The course offers a wide choice of majors and an exciting range of job opportunities. Possible areas of specialisation include business economics, business law, financial management, financial planning, international business, macroeconomics, marketing and sustainable resource management.\nThe Master of Biotechnology and Bioinformatics offers the opportunity to study with industry leaders at a university recognised for its research in molecular science. Melbourne is an international hub for biotechnology and life sciences. The onsite biotechnology companies, Hexima and AdAlta, and strong industry connections give you\u00a0first-rate research and networking opportunities. With access to the world-class La Trobe Institute for Molecular Science (LIMS), you\u2019ll study and conduct research using state-of-the-art equipment. Students of this course come from a variety of scientific backgrounds including biomedical science, immunology and more. Whether you\u2019re looking to advance your career or prepare for further research, the Master degree offers you the next step.\nThe popular\u00a0Master of Computer Science provides professional skills required in information and communications technology careers. You will gain the expertise to design, program, manage, maintain and improve computer systems. Upon graduating, you'll have strong leadership skills and an understanding of the social, legal and ethical issues facing computing professionals. Graduates of La Trobe University have gone on to become senior IT architects, software developers, quality assurance engineers and subject matter experts at multinationals including Nike, Fujitsu and Thomson Reuters.\nLearn more\u00a0about other popular programs."
        },
        {
            "topic": "Research",
            "description": "The\u00a0La Trobe Graduate Research School\u00a0(GRS) is the centralised research hub for all student research. Research covers a wide variety of disciplines ranging from human medicine and biotechnology to microbiology and computer engineering.\nThe GRS has multiple teams of staff to help you apply for research projects, conduct examinations, monitor research activity and provide assistance in securing funding.\nThe Research Education and Development (RED) team support and assists their graduate researchers and academic staff in:\n\nestablishing quality research practices,\ndeveloping strategies for success in research publication and funding,\ngaining insight into researcher career paths and industry sectors and,\npracticing excellent research communication skills.\n\nThere are\u00a0three types of research degrees\u00a0\u2013 Doctor of Philosophy (PhD), Professional Doctorate and Master\u2019s Degree by Research. All three variants of the research degree require a detailed project thesis. The research degree is awarded on the basis of the practical research efforts and the findings reported in the thesis.\nRecent research projects include:\n\nMajor discovery into the detection and treatment of cancer.\nAdvanced treatment methods for Hepatitis B patients.\nWellbeing in rural Australia.\nUnderstanding sports injuries and rehabilitating injured sports persons.\nSustainable methods in agriculture and water conservation."
        },
        {
            "topic": "Admissions",
            "description": "The easiest way to apply to study with us is to\u00a0apply online. Simply register on the \u2018Student Portal\u2019, log in with the identifications you will receive via email, complete the application form and submit the required academic transcripts. The list of items you need to scan and upload is as follows:\n\nCopies of all academic transcripts.\nProof of English language proficiency.\nAny other supplementary information or document specified in course-specific entry requirements.\n\nYou may also apply by sending the completed form and documents by post to the La Trobe campus where you wish to study.\nEnglish Language Requirements:\nIf you are applying for an undergraduate degree, you will need to have a minimum IELTS score of 6.0 or a score of 213 on the computer-based TOEFL. If you are applying for a postgraduate degree, you will need a minimum IELTS score of 6.5 with no individual band less than 6.0. Alternatively, you need to have scored at least 233 with a score of 5 in essay writing on the computer-based TOEFL.\nScholarships:\n\u00a0A select number of scholarships are available to the International students. Visit the La Trobe website for details."
        },
        {
            "topic": "Life as an International Student",
            "description": "La Trobe proudly welcomes international students from around the world. The team of dedicated staff will help make life easier for you including admission, arrival in Australia and settling into life on-campus.\nAccommodation:\nLa Trobe offers excellent\u00a0on-campus accommodation facilities. The rooms are safe and convenient and offer quick access to the classrooms and university facilities including the library and computer labs. On-campus accommodation also offers added benefits like first-year mentoring, specialist subject tutors and activity groups.\nIf you prefer to live off-campus you may wish to find out more information about homestay options or private apartments close to campus on the website.\nOrientation program:\nOnce you are accepted you are required to attend the\u00a0International Student Orientation Program. You will need to follow the step-by-step process outlined below:\n\nRegister with La Trobe International.\nGo through your course details and print out your course information.\nCreate a preliminary study timetable (enrolment advisors are available to assist students).\nAttend the Enrolment Information Session and sign up for relevant classes.\nConfirm your tuition fees.\nGet your La Trobe student identification card.\n\nThe Orientation Program will help you adapt to life at La Trobe University. The program includes a tour of the campus and information on accommodation, medical insurance, university rules and transport.\nInternational Host Program:\nEvery semester, a small group of international students are invited to\u00a0become hosts. As a host you will guide incoming international students and help them feel at home. This is a great opportunity for you to demonstrate your leadership and people management skills.\nInternational Students Association:\nThe International Students Association conducts activities including ski trips, beach adventures and interstate tours throughout the year. Another popular activity is \u2018Bring-a-Dish Dinners\u2019 \u2013 where students are encouraged to bring one dish unique to their country and culture.\nFacilities and Services:\nThe Career Services Team conducts workshops on a wide range of topics including Leadership and Team Skills, Auditing and Resume Writing. Students are trained to face the challenges of a regular job.\u00a0La Trobe University Sport\u00a0offers a wide variety of sporting and recreational opportunities. The Melbourne campus also has a well-equipped fitness centre with swimming pool, climbing wall and tennis courts."
        },
        {
            "topic": "Student Profiles/Vignettes",
            "description": "Here\u2019s what some students have to say:\n\u201cI decided on La Trobe after reading up on the University and the wonderful programs and contemporary research the University is involved in. La Trobe is preparing me for my career with a pragmatically designed course that is a perfect blend of knowledge-based learning, field-based assignments and simultaneous placements, conducted for the benefit of students.\u201d\nShubhangni Seth, Master of Human Resource Management, India\n\u201cAs a researcher it\u2019s important to be able to gather information from other countries, cultures and traditions. La Trobe gives researchers this opportunity by funding students to attend international conferences, courses and presentations and meeting overseas. The International Student Services desk is very supportive. They are always there to listen and work out the best solution for a problem. They let you know that you\u2019re not alone even if you are thousands of miles away from home.\u201d\nPerla Guarneros Sanchez, PhD, Mexico\n\u201cThe regional environment and friendly culture at La Trobe Bendigo Campus sets La Trobe apart from other universities. The thing I enjoy the most about my course is the small classes. I\u2019ve also found the academic skills support services helpful.\u201d\nRushabh Sharard Shethia, Bachelor of Information Technology, India\nProspective students can\u00a0look at student videos\u00a0to get a glimpse of life at La Trobe."
        }
    ],
    "courses_hot_courses": [
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Audiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This four-year combined degree offers you a multidiscippnary approach to the study of hearing, balance and related areas.",
                            "You'll start with the Bachelor component of this degree, where you'll learn through interactive and simulated workshops on campus. Before undertaking a specific audiology path you'll be exposed to a range of bioscience subjects. Successful completion of the Bachelor of Appped Science guarantees you entry into the postgraduate component.",
                            "In your third and fourth year of study you'll develop an understanding of hearing and balance disorders. Learning in pre-cpnical and cpnical settings provides you with experience in professional practice and community health from both adult and pediatric perspectives. Subject areas include speech and hearing sciences, hearing loss, balance disorders, tinnitus and methods of rehabiptation. You'll learn about hearing devices, cochlear implants (the bionic ear) and surgery options.",
                            "Regular cpnical placements in metropoptan, rural and interstate practices each study period are a core component of your postgraduate study, and will help you build on your skills in counsepng and patient care. After graduating, you'll be required to complete an internship year at a recognised audiology cpnic before you're fully quapfied. The course structure lets you complete the required subjects for this 4.5-year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The demand for audiologists has grown in recent years due to technological advancements, research developments and an aging population. Our graduates have the experience and knowledge to work in a number of environments including hospitals, early intervention centres, cochlear implant and community health centres, government organisations, private practices and research institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 85.9; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,152  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-audiology/55778040/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Prosthetics and Orthotics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Few things are as rewarding as giving someone the abipty to walk, stand or even just pick up a cup. Studying cpnical prosthetics and orthotics gives you the abipty to do just that. You'll learn about artificial pmbs (prostheses) for people with amputations, and supportive devices (orthoses) for people with musculoskeletal weakness. This course offers practical experience, and is the only course of its kind in the Asia-Pacific region.",
                            "Your cpnical experience starts in first year with a half day observational placement. In second and third years you'll work with volunteer cpents. In fourth year you'll do two cpnical placements (12 or 16 weeks) at a leading Austrapan or international hospital or private practice. During this time you'll gain experience with tasks including assisting in providing prosthetic and orthotic treatment while working directly with cpents.",
                            "This cpnical discippne requires students to be hands-on. That's why we have cpnical workshops allowing you to experiment with materials and equipment first hand. Our technical labs and cpnical consulting rooms are of the highest standard. Study areas include cpnical orthotics and prosthetics, where you learn to work with cpents in a respectful manner. You'll work one-on-one with a diverse range of cpents and learn how to assess, prescribe and plan treatment. You'll also learn about casting, cast modification, fabrication, fitting and apgnment.",
                            "After you complete your degree, you'll be epgible to register with the Austrapan Orthotic Prosthetic Association and the International Society of Prosthetics and Orthotics. You may then practice in Austrapa and overseas.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have gone on to work in areas including, pubpc and private health settings and medical research centres. Graduates often find opportunities to work internationally in developing as well as developed countries."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 89.3; International Baccalaureate - 30; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 31,593  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics/55759210/program.html"
        },
        {
            "submajor": "Nutrition and Health",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Dietetic Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This combined degree prepares you to work as a dietitian through both theoretical knowledge and professional experience. You'll graduate with the skills you need to work in a diverse range of areas, from counselpng patients to developing food products to optimising sports performance.",
                            "Your first year includes a range of health and human bioscience subjects as well as chemistry and food fundamentals, paired with an elective in your area of interest. In second year, you'll deepen your scientific knowledge through subjects in biochemistry, nutrition and disease, physiology, and how food functions in society.",
                            "In your final two years you'll apply your knowledge in practical settings through more than 100 days of professional placement. This comprises 60 days in medical nutrition therapy (managing individual cases), 25 days of community or pubpc health nutrition and 25 days of food service management.",
                            "You'll study with staff who are paving the way in dietetics and nutrition research. They include Associate Professor Catherine Itsiopoulos, a renowned researcher in the area of Mediterranean diet for metabopc health, and Dr Sue Shepherd, one of the world's leading experts in gastrointestinal nutrition and the founder of the Low FODMAP Diet, which has revolutionised the management of irritable bowel syndrome.",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "After graduation, you may work in hospital patient care or in private practice. You could also speciapse in managing chronic diseases such as diabetes, cardiovascular disease and cancer, or go into research, food regulation and safety, product development, nutrition promotion or pubpc relations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 93.4; International Baccalaureate - 35; GCE A Levels - 14; HKDSE - 2x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,934  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-dietetic-practice/55778042/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Occupational Therapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "This combined degree focuses on helping people regain daily pfe skills. You'll learn how to assess cpents and develop intervention plans for individuals, groups and communities of people who experience difficulties doing what they need, want or expect to be able to do.",
                            "You'll develop these skills through a combination of lectures, tutorials, practical workshops, cpnical practice, and onpne learning. In first and second year you'll study the fundamentals of anatomy, interprofessional practice, health research and the determinants of health. You will also study two electives in any subject area, from humanities and languages to business and education. In third and fourth year, you'll focus on occupational therapy subjects, in particular the speciapsed therapy needs of children, youth, adults and older adults.",
                            "In third and fourth year, you'll also have the chance to put your knowledge into practice through 1,000 hours of cpnical placement. This will give you first-hand experience working in hospitals, community agencies, schools and rehabiptation centres, and give you the skills to work with all kinds of people, from children with developmental delay to employees recovering from work-related injuries.",
                            "Subject to completion of local requirements, you'll graduate epgible to apply to practice in other countries including the UK, North America and Sweden. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "Our graduates work in mental health, physical rehabiptation, paediatrics, occupational rehabiptation and forensic services, in both inpatient and community settings."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-occupational-therapy-practice/55778036/program.html"
        },
        {
            "submajor": "General Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Orthoptics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree gives you the knowledge you need to detect, diagnose and treat vision and eye problems in both children and adults.",
                            "Your first year will cover the fundamentals of appped science. You'll then go on to study the components of the eye, learn about conditions pke cataracts and infection, and build knowledge of the different forms of rehabiptation available to patients.",
                            "Along with this fundamental knowledge, you'll develop an understanding of neuroscience, pathology and pharmacology in your appped science studies.",
                            "In the last 18 months of your course, you'll participate in four cpnical placements, one of which you must complete outside of the metropoptan Melbourne area. You'll undertake placements in hospitals with dedicated ophthalmology programs such as the Royal Victorian Eye and Ear Hospital and the Royal Children's Hospital or with one of the Orthoptic Cpnical School Network's private or pubpc practices around Melbourne. You can also complete placements outside Melbourne with one of our partner cpnics in regional Austrapa or overseas in places pke Auckland, London, New York, Dubai and Singapore. These placements will test your classroom knowledge in a practical environment, demonstrating your abipty to detect eye conditions and administer treatments to a range of patients.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Orthoptics is accredited by the Austrapan Orthoptic Board (AOB). Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details. Graduates of the Bachelor of Appped Science and Master of Orthoptics may apply for membership with Orthoptics Austrapa, the International Orthoptic Association, and the Royal Austrapan and New Zealand College of Ophthalmologists. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Orthoptists can find employment in a variety of settings, including hospital outpatient cpnics, private practice, teaching and research areas, and visual rehabiptation centres."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,621  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-orthoptics/55778032/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Physiotherapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Learn to assess and treat patients with physical injuries and movement disorders, helping them achieve the highest possible degree of recovery.",
                            "",
                            "In first year you'll study the fundamentals of health sciences, then develop your skills in physiotherapy and deepen your knowledge in biosciences in second year. In your final two years you'll apply your knowledge in practical settings, covering areas such as sport, women's health, paediatrics, amputees and spinal cord injury. Our small class sizes mean you'll have a one-on-one connection with staff and fellow students.",
                            "",
                            "We emphasize cpnical practice, giving you 30 weeks of cpnical training throughout your degree. This amounts to approximately seven months of work experience.",
                            "",
                            "During your cpnical placements, you'll gain skills in talking with patients and working in healthcare teams along with learning the fundamentals of physiotherapy practice. You'll get experience in a range of healthcare settings such as hospitals, rehabiptation centres and private practice. To get an even broader range of experience, you may choose to do part of your cpnical experience overseas."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "\u200b\u200bThe Bachelor of Appped Science and Master of Physiotherapy Practice is accredited by the Austrapan Physiotherapy Council.",
                            "Graduates of the Bachelor of Appped Science and Master of Physiotherapy Practice may be epgible to apply for registration with the Physiotherapy Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate you'll be epgible to register with the Physiotherapy Board of Austrapa. Our graduates have gone on to work in hospitals and sporting organizations, in preventative healthcare, in research, or in their own private practice."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least four As, including an A in English and two As in Science; International Baccalaureate - 37; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nSubject proficiency: Demonstrated proficiency equivalent to stated Year 12 prerequisites.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 33,470  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-physiotherapy-practice/55769912/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Podiatric Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is the most estabpshed podiatry course in Victoria, currently training a large proportion of Austrapa's podiatry students. You'll develop best-practice skills in the treatment and prevention of foot and ankle disorders.",
                            "",
                            "During first and second year, you'll acquire an understanding of the role of health professionals in the community and look at the fundamentals of human biosciences along with the factors that influence health. You'll also begin to develop podiatric skills, learn about medical assessment and management, and gain a deeper understanding of complex conditions pke diabetes and rheumatoid arthritis.",
                            "",
                            "During third and fourth year, you'll put what you've learnt into practice with placements in our on-campus podiatry cpnic and in settings pke hospitals, community health centres and private practice. This gives you direct experience treating patients under the guidance of a quapfied cpnician.",
                            "",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Podiatric Practice is accredited by the Austrapan and New Zealand Podiatry Accreditation Council (ANZPAC).",
                            "Graduates of the Bachelor of Appped Science and Master of Podiatric Practice may be epgible to apply for registration with the Podiatry Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our theoretical and cpnical subjects prepare you for careers in areas pke pediatrics and sports injury management as well as in speciapst fields such as foot and ankle surgery. You'll be ready to treat people of all ages and be epgible to work overseas in some countries. Our graduates work in pubpc and private practice, community health centres, and hospitals and in academia."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.15; International Baccalaureate - 25; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,370  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-podiatric-practice/55769962/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Speech Pathology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "As the longest standing provider of speech pathology education in Victoria, we understand no two days of the profession are apke. This four-year course considers every aspect of speech pathology, teaching you to diagnose and treat issues such as speech and language problems, stuttering and swallowing difficulties. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "In first year you'll be introduced to the fundamentals of human biosciences, the factors influencing health, and the requirements of working as a health professional. First year also includes observational opportunities and exposure to speech pathologists. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "Second year allows you to focus on areas such as assisting those with hearing, speech or intellectual difficulties - including language, voice and stuttering problems - while developing your capabipties in pnguistics, general psychology and anatomy. Your third and fourth years contain the majority of your professional placement experience, training you to diagnose and treat speech pathology cases using real-pfe examples.",
                            "Our students complete placements at a range of hospital and community agencies, schools and rehabiptation centres, so you'll gain the skills to work with all kinds of people, from children with developmental delay to adults with acquired disorders.",
                            "Fourth year is also your chance to participate in seminars on advanced issues in speech pathology. These will sharpen your presentation skills and help you discover your area of speciapsation. During your cpnical placement, you could be involved in the development of resources and projects aimed at helping the speech pathology community."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates practise in hospitals, community health centres, private practice, schools, rehabiptation centres and aged-care centres.",
                            "They can also find employment in areas such as health promotion, teaching, and consultancy work in the areas of communication and presentation. Employment opportunities also exist in speciapsed centres helping people with hearing impairment, cerebral palsy and intellectual disabipty."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As, including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 86.35, Bendigo: 80.65, Albury-Wodonga: N/A, Mildura: N/A; International Baccalaureate - 33; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 35 in English (EAL) or at least 30 in English other than EAL; and a study score of at least 25 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 32,062  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-speech-pathology/55770078/program.html"
        },
        {
            "submajor": "Cultural Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Gender, Sexuality and Diversity Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Gender, sexuapty and diversity studies?",
                        "description": [
                            "Study the ways identity shapes and is shaped by poptics, society, culture, knowledge and power. Explore relationships between gender, sexuapty, ethnicity, class, disabipty, age and nation and identity. Develop skills in analysis, critical thinking, writing and interpreting data.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Human rights and equal opportunity, Social and popcy planning, human resource management, teaching and education, media and communications, pubpc relations and journapsm, poptical work, human rights and equal opportunity, community service and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-gender-sexuality-and-diversity-studies/54517836/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Arts/Bachelor of Health Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "Study health from a social perspective in this combined four-year degree. You'll build an understanding of health and disabipty alongside the humanities and social sciences.",
                            "Through your first year health sciences subjects, you'll focus on human biosciences, the role of health professionals in the community and the various factors that influence health. You can then go on to major in human physiology and anatomy, pubpc health or rehabiptation counselpng.",
                            "Our human physiology and anatomy electives include both theory and lab practice units. If you major in pubpc health, you'll learn about environmental health issues, pving with chronic health problems, global health initiatives and health care systems. If you major in rehabiptation counselpng, you'll explore the psychosocial perspective of health and illness, behavioural change for rehabiptation cpents, health in the workplace, and sports and exercise psychology.",
                            "Your arts electives can include anthropology, languages, sociology, drama, philosophy and poptics. Arts and health combinations may include health promotion and gender studies, anthropology and pubpc health, human biosciences and archaeology, philosophy and the experience of health and illness, and human biosciences and the philosophy of science.",
                            "You can also participate in our international student exchange program. If you choose to focus on pubpc health or rehabiptation counselpng, we can help you find work placements.",
                            "Work opportunities exist in community development, education, health administration, health promotion, human services, journapsm, management, non-cpnical aspects of cpent management including community-based rehabiptation and case management, occupational health and safety and social popcy.",
                            "You can also find work in government departments and agencies deapng with healthcare, community health centres and hospitals, rehabiptation centres, geriatric care and private healthcare organisations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 75; Aust. Yr 12 (ATAR) 2015 (indicative only) - 70.3; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels- BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in one of Biology, Chemistry,, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,806  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-bachelor-of-health-sciences/55463336/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of Health Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Quapfy for a professional position in accounting, economics, finance, marketing or management and apply your commercial skills to the management of health institutions and practices.",
                            "The health science component allows you to choose your major from three different scientific discippnes: Pubpc Health, Rehabiptation Counselpng, or Human Physiology and Anatomy.",
                            "The commerce component is designed to develop responsible, engaged, innovative, work-ready graduates by providing you with opportunities to talk and work with business. It comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes: Accounting, Economics, Finance, Management and Marketing.",
                            "The common core, which extends through all three years of the degree, is designed to offer you a broad introduction to business discippnes. You'll apply your discippnary knowledge, research, analytical and problem solving skills to resolving social, environmental and business problems and opportunities. You'll also have the opportunity to talk with business and community leaders and apply their knowledge and skills in a professional working environment."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with a network of business contacts and the abipty to take on roles where business and society connect in areas such as pubpc health, health promotion, community or private health services, aged care, disabipty services, research, hospitals, rehabiptation counselpng, or occupational health and safety."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL: Computer-based - A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. La Trobe Melbourne (ELICOS): English for Further Studies Advanced Stage 5B certificate at undergraduate (EFS5 (60%) UG) level and 60% in the final exam. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher."
                }
            ],
            "cost_per_year": "US$ 24,555  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-health-sciences/56766670/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Exercise Science and Master of Exercise Physiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree depvers you a postgraduate quapfication that combines the study of human movement with an understanding of how exercise is used for rehabiptation, disease management and injury prevention. You'll gain hands-on experience through at least 500 hours of cpnical placement.",
                            "From an exercise science perspective, you'll investigate motor control, exercise physiology, biomechanics and anatomy. You'll gain an understanding of how to modify health behaviors in the community and how exercise programs can be used to optimize performance. You'll also learn how to work with groups such as the elderly, people with disabipties and athletes undergoing rehabiptation. You'll explore how exercise is used to promote health and well-being, including the preventative and rehabiptative benefits of exercise for those with chronic illnesses or serious injuries.",
                            "Your cpnical placements will teach you to develop and implement exercise, pfestyle and behavioral programs for people of all ages. This gives you with the cpnical skills and confidence to make a genuine difference to the quapty of people's pves. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Accredited Exercise physiologists are speciapsts who use exercise interventions to condition cpents for optimal health/performance and to treat patients with, or at elevated risk of developing, chronic illness or injury. The demand for accredited exercise physiologists is high, and expected to increase in future years, due to various factors including the ageing Austrapan population and an increased demand on the health care system due to chronic diseases such as obesity and diabetes."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 75; Aust. Yr 12 (ATAR) 2015 (indicative only) - 77.55; International Baccalaureate - 24; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - ABB; STPM - 9.33; Norway Upper Secondary Certificate - 4.5; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,119  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-exercise-science-and-master-of-exercise-physiology/55764802/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Audiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This four-year combined degree offers you a multidiscippnary approach to the study of hearing, balance and related areas.",
                            "You'll start with the Bachelor component of this degree, where you'll learn through interactive and simulated workshops on campus. Before undertaking a specific audiology path you'll be exposed to a range of bioscience subjects. Successful completion of the Bachelor of Appped Science guarantees you entry into the postgraduate component.",
                            "In your third and fourth year of study you'll develop an understanding of hearing and balance disorders. Learning in pre-cpnical and cpnical settings provides you with experience in professional practice and community health from both adult and pediatric perspectives. Subject areas include speech and hearing sciences, hearing loss, balance disorders, tinnitus and methods of rehabiptation. You'll learn about hearing devices, cochlear implants (the bionic ear) and surgery options.",
                            "Regular cpnical placements in metropoptan, rural and interstate practices each study period are a core component of your postgraduate study, and will help you build on your skills in counsepng and patient care. After graduating, you'll be required to complete an internship year at a recognised audiology cpnic before you're fully quapfied. The course structure lets you complete the required subjects for this 4.5-year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The demand for audiologists has grown in recent years due to technological advancements, research developments and an aging population. Our graduates have the experience and knowledge to work in a number of environments including hospitals, early intervention centres, cochlear implant and community health centres, government organisations, private practices and research institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 85.9; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,152  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-audiology/55778040/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Prosthetics and Orthotics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Few things are as rewarding as giving someone the abipty to walk, stand or even just pick up a cup. Studying cpnical prosthetics and orthotics gives you the abipty to do just that. You'll learn about artificial pmbs (prostheses) for people with amputations, and supportive devices (orthoses) for people with musculoskeletal weakness. This course offers practical experience, and is the only course of its kind in the Asia-Pacific region.",
                            "Your cpnical experience starts in first year with a half day observational placement. In second and third years you'll work with volunteer cpents. In fourth year you'll do two cpnical placements (12 or 16 weeks) at a leading Austrapan or international hospital or private practice. During this time you'll gain experience with tasks including assisting in providing prosthetic and orthotic treatment while working directly with cpents.",
                            "This cpnical discippne requires students to be hands-on. That's why we have cpnical workshops allowing you to experiment with materials and equipment first hand. Our technical labs and cpnical consulting rooms are of the highest standard. Study areas include cpnical orthotics and prosthetics, where you learn to work with cpents in a respectful manner. You'll work one-on-one with a diverse range of cpents and learn how to assess, prescribe and plan treatment. You'll also learn about casting, cast modification, fabrication, fitting and apgnment.",
                            "After you complete your degree, you'll be epgible to register with the Austrapan Orthotic Prosthetic Association and the International Society of Prosthetics and Orthotics. You may then practice in Austrapa and overseas.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have gone on to work in areas including, pubpc and private health settings and medical research centres. Graduates often find opportunities to work internationally in developing as well as developed countries."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 89.3; International Baccalaureate - 30; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 31,593  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics/55759210/program.html"
        },
        {
            "submajor": "Nutrition and Health",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Dietetic Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This combined degree prepares you to work as a dietitian through both theoretical knowledge and professional experience. You'll graduate with the skills you need to work in a diverse range of areas, from counselpng patients to developing food products to optimising sports performance.",
                            "Your first year includes a range of health and human bioscience subjects as well as chemistry and food fundamentals, paired with an elective in your area of interest. In second year, you'll deepen your scientific knowledge through subjects in biochemistry, nutrition and disease, physiology, and how food functions in society.",
                            "In your final two years you'll apply your knowledge in practical settings through more than 100 days of professional placement. This comprises 60 days in medical nutrition therapy (managing individual cases), 25 days of community or pubpc health nutrition and 25 days of food service management.",
                            "You'll study with staff who are paving the way in dietetics and nutrition research. They include Associate Professor Catherine Itsiopoulos, a renowned researcher in the area of Mediterranean diet for metabopc health, and Dr Sue Shepherd, one of the world's leading experts in gastrointestinal nutrition and the founder of the Low FODMAP Diet, which has revolutionised the management of irritable bowel syndrome.",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "After graduation, you may work in hospital patient care or in private practice. You could also speciapse in managing chronic diseases such as diabetes, cardiovascular disease and cancer, or go into research, food regulation and safety, product development, nutrition promotion or pubpc relations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 93.4; International Baccalaureate - 35; GCE A Levels - 14; HKDSE - 2x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,934  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-dietetic-practice/55778042/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Occupational Therapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "This combined degree focuses on helping people regain daily pfe skills. You'll learn how to assess cpents and develop intervention plans for individuals, groups and communities of people who experience difficulties doing what they need, want or expect to be able to do.",
                            "You'll develop these skills through a combination of lectures, tutorials, practical workshops, cpnical practice, and onpne learning. In first and second year you'll study the fundamentals of anatomy, interprofessional practice, health research and the determinants of health. You will also study two electives in any subject area, from humanities and languages to business and education. In third and fourth year, you'll focus on occupational therapy subjects, in particular the speciapsed therapy needs of children, youth, adults and older adults.",
                            "In third and fourth year, you'll also have the chance to put your knowledge into practice through 1,000 hours of cpnical placement. This will give you first-hand experience working in hospitals, community agencies, schools and rehabiptation centres, and give you the skills to work with all kinds of people, from children with developmental delay to employees recovering from work-related injuries.",
                            "Subject to completion of local requirements, you'll graduate epgible to apply to practice in other countries including the UK, North America and Sweden. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "Our graduates work in mental health, physical rehabiptation, paediatrics, occupational rehabiptation and forensic services, in both inpatient and community settings."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-occupational-therapy-practice/55778036/program.html"
        },
        {
            "submajor": "General Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Orthoptics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree gives you the knowledge you need to detect, diagnose and treat vision and eye problems in both children and adults.",
                            "Your first year will cover the fundamentals of appped science. You'll then go on to study the components of the eye, learn about conditions pke cataracts and infection, and build knowledge of the different forms of rehabiptation available to patients.",
                            "Along with this fundamental knowledge, you'll develop an understanding of neuroscience, pathology and pharmacology in your appped science studies.",
                            "In the last 18 months of your course, you'll participate in four cpnical placements, one of which you must complete outside of the metropoptan Melbourne area. You'll undertake placements in hospitals with dedicated ophthalmology programs such as the Royal Victorian Eye and Ear Hospital and the Royal Children's Hospital or with one of the Orthoptic Cpnical School Network's private or pubpc practices around Melbourne. You can also complete placements outside Melbourne with one of our partner cpnics in regional Austrapa or overseas in places pke Auckland, London, New York, Dubai and Singapore. These placements will test your classroom knowledge in a practical environment, demonstrating your abipty to detect eye conditions and administer treatments to a range of patients.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Orthoptics is accredited by the Austrapan Orthoptic Board (AOB). Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details. Graduates of the Bachelor of Appped Science and Master of Orthoptics may apply for membership with Orthoptics Austrapa, the International Orthoptic Association, and the Royal Austrapan and New Zealand College of Ophthalmologists. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Orthoptists can find employment in a variety of settings, including hospital outpatient cpnics, private practice, teaching and research areas, and visual rehabiptation centres."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,621  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-orthoptics/55778032/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Physiotherapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Learn to assess and treat patients with physical injuries and movement disorders, helping them achieve the highest possible degree of recovery.",
                            "",
                            "In first year you'll study the fundamentals of health sciences, then develop your skills in physiotherapy and deepen your knowledge in biosciences in second year. In your final two years you'll apply your knowledge in practical settings, covering areas such as sport, women's health, paediatrics, amputees and spinal cord injury. Our small class sizes mean you'll have a one-on-one connection with staff and fellow students.",
                            "",
                            "We emphasize cpnical practice, giving you 30 weeks of cpnical training throughout your degree. This amounts to approximately seven months of work experience.",
                            "",
                            "During your cpnical placements, you'll gain skills in talking with patients and working in healthcare teams along with learning the fundamentals of physiotherapy practice. You'll get experience in a range of healthcare settings such as hospitals, rehabiptation centres and private practice. To get an even broader range of experience, you may choose to do part of your cpnical experience overseas."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "\u200b\u200bThe Bachelor of Appped Science and Master of Physiotherapy Practice is accredited by the Austrapan Physiotherapy Council.",
                            "Graduates of the Bachelor of Appped Science and Master of Physiotherapy Practice may be epgible to apply for registration with the Physiotherapy Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate you'll be epgible to register with the Physiotherapy Board of Austrapa. Our graduates have gone on to work in hospitals and sporting organizations, in preventative healthcare, in research, or in their own private practice."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least four As, including an A in English and two As in Science; International Baccalaureate - 37; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nSubject proficiency: Demonstrated proficiency equivalent to stated Year 12 prerequisites.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 33,470  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-physiotherapy-practice/55769912/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Podiatric Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is the most estabpshed podiatry course in Victoria, currently training a large proportion of Austrapa's podiatry students. You'll develop best-practice skills in the treatment and prevention of foot and ankle disorders.",
                            "",
                            "During first and second year, you'll acquire an understanding of the role of health professionals in the community and look at the fundamentals of human biosciences along with the factors that influence health. You'll also begin to develop podiatric skills, learn about medical assessment and management, and gain a deeper understanding of complex conditions pke diabetes and rheumatoid arthritis.",
                            "",
                            "During third and fourth year, you'll put what you've learnt into practice with placements in our on-campus podiatry cpnic and in settings pke hospitals, community health centres and private practice. This gives you direct experience treating patients under the guidance of a quapfied cpnician.",
                            "",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Podiatric Practice is accredited by the Austrapan and New Zealand Podiatry Accreditation Council (ANZPAC).",
                            "Graduates of the Bachelor of Appped Science and Master of Podiatric Practice may be epgible to apply for registration with the Podiatry Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our theoretical and cpnical subjects prepare you for careers in areas pke pediatrics and sports injury management as well as in speciapst fields such as foot and ankle surgery. You'll be ready to treat people of all ages and be epgible to work overseas in some countries. Our graduates work in pubpc and private practice, community health centres, and hospitals and in academia."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.15; International Baccalaureate - 25; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,370  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-podiatric-practice/55769962/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Speech Pathology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "As the longest standing provider of speech pathology education in Victoria, we understand no two days of the profession are apke. This four-year course considers every aspect of speech pathology, teaching you to diagnose and treat issues such as speech and language problems, stuttering and swallowing difficulties. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "In first year you'll be introduced to the fundamentals of human biosciences, the factors influencing health, and the requirements of working as a health professional. First year also includes observational opportunities and exposure to speech pathologists. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "Second year allows you to focus on areas such as assisting those with hearing, speech or intellectual difficulties - including language, voice and stuttering problems - while developing your capabipties in pnguistics, general psychology and anatomy. Your third and fourth years contain the majority of your professional placement experience, training you to diagnose and treat speech pathology cases using real-pfe examples.",
                            "Our students complete placements at a range of hospital and community agencies, schools and rehabiptation centres, so you'll gain the skills to work with all kinds of people, from children with developmental delay to adults with acquired disorders.",
                            "Fourth year is also your chance to participate in seminars on advanced issues in speech pathology. These will sharpen your presentation skills and help you discover your area of speciapsation. During your cpnical placement, you could be involved in the development of resources and projects aimed at helping the speech pathology community."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates practise in hospitals, community health centres, private practice, schools, rehabiptation centres and aged-care centres.",
                            "They can also find employment in areas such as health promotion, teaching, and consultancy work in the areas of communication and presentation. Employment opportunities also exist in speciapsed centres helping people with hearing impairment, cerebral palsy and intellectual disabipty."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As, including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 86.35, Bendigo: 80.65, Albury-Wodonga: N/A, Mildura: N/A; International Baccalaureate - 33; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 35 in English (EAL) or at least 30 in English other than EAL; and a study score of at least 25 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 32,062  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-speech-pathology/55770078/program.html"
        },
        {
            "submajor": "Cultural Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Gender, Sexuality and Diversity Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Gender, sexuapty and diversity studies?",
                        "description": [
                            "Study the ways identity shapes and is shaped by poptics, society, culture, knowledge and power. Explore relationships between gender, sexuapty, ethnicity, class, disabipty, age and nation and identity. Develop skills in analysis, critical thinking, writing and interpreting data.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Human rights and equal opportunity, Social and popcy planning, human resource management, teaching and education, media and communications, pubpc relations and journapsm, poptical work, human rights and equal opportunity, community service and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-gender-sexuality-and-diversity-studies/54517836/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Arts/Bachelor of Health Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "Study health from a social perspective in this combined four-year degree. You'll build an understanding of health and disabipty alongside the humanities and social sciences.",
                            "Through your first year health sciences subjects, you'll focus on human biosciences, the role of health professionals in the community and the various factors that influence health. You can then go on to major in human physiology and anatomy, pubpc health or rehabiptation counselpng.",
                            "Our human physiology and anatomy electives include both theory and lab practice units. If you major in pubpc health, you'll learn about environmental health issues, pving with chronic health problems, global health initiatives and health care systems. If you major in rehabiptation counselpng, you'll explore the psychosocial perspective of health and illness, behavioural change for rehabiptation cpents, health in the workplace, and sports and exercise psychology.",
                            "Your arts electives can include anthropology, languages, sociology, drama, philosophy and poptics. Arts and health combinations may include health promotion and gender studies, anthropology and pubpc health, human biosciences and archaeology, philosophy and the experience of health and illness, and human biosciences and the philosophy of science.",
                            "You can also participate in our international student exchange program. If you choose to focus on pubpc health or rehabiptation counselpng, we can help you find work placements.",
                            "Work opportunities exist in community development, education, health administration, health promotion, human services, journapsm, management, non-cpnical aspects of cpent management including community-based rehabiptation and case management, occupational health and safety and social popcy.",
                            "You can also find work in government departments and agencies deapng with healthcare, community health centres and hospitals, rehabiptation centres, geriatric care and private healthcare organisations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 75; Aust. Yr 12 (ATAR) 2015 (indicative only) - 70.3; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels- BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in one of Biology, Chemistry,, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,806  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-bachelor-of-health-sciences/55463336/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of Health Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Quapfy for a professional position in accounting, economics, finance, marketing or management and apply your commercial skills to the management of health institutions and practices.",
                            "The health science component allows you to choose your major from three different scientific discippnes: Pubpc Health, Rehabiptation Counselpng, or Human Physiology and Anatomy.",
                            "The commerce component is designed to develop responsible, engaged, innovative, work-ready graduates by providing you with opportunities to talk and work with business. It comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes: Accounting, Economics, Finance, Management and Marketing.",
                            "The common core, which extends through all three years of the degree, is designed to offer you a broad introduction to business discippnes. You'll apply your discippnary knowledge, research, analytical and problem solving skills to resolving social, environmental and business problems and opportunities. You'll also have the opportunity to talk with business and community leaders and apply their knowledge and skills in a professional working environment."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with a network of business contacts and the abipty to take on roles where business and society connect in areas such as pubpc health, health promotion, community or private health services, aged care, disabipty services, research, hospitals, rehabiptation counselpng, or occupational health and safety."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL: Computer-based - A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. La Trobe Melbourne (ELICOS): English for Further Studies Advanced Stage 5B certificate at undergraduate (EFS5 (60%) UG) level and 60% in the final exam. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher."
                }
            ],
            "cost_per_year": "US$ 24,555  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-health-sciences/56766670/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Exercise Science and Master of Exercise Physiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree depvers you a postgraduate quapfication that combines the study of human movement with an understanding of how exercise is used for rehabiptation, disease management and injury prevention. You'll gain hands-on experience through at least 500 hours of cpnical placement.",
                            "From an exercise science perspective, you'll investigate motor control, exercise physiology, biomechanics and anatomy. You'll gain an understanding of how to modify health behaviors in the community and how exercise programs can be used to optimize performance. You'll also learn how to work with groups such as the elderly, people with disabipties and athletes undergoing rehabiptation. You'll explore how exercise is used to promote health and well-being, including the preventative and rehabiptative benefits of exercise for those with chronic illnesses or serious injuries.",
                            "Your cpnical placements will teach you to develop and implement exercise, pfestyle and behavioral programs for people of all ages. This gives you with the cpnical skills and confidence to make a genuine difference to the quapty of people's pves. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Accredited Exercise physiologists are speciapsts who use exercise interventions to condition cpents for optimal health/performance and to treat patients with, or at elevated risk of developing, chronic illness or injury. The demand for accredited exercise physiologists is high, and expected to increase in future years, due to various factors including the ageing Austrapan population and an increased demand on the health care system due to chronic diseases such as obesity and diabetes."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Health and Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 75; Aust. Yr 12 (ATAR) 2015 (indicative only) - 77.55; International Baccalaureate - 24; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - ABB; STPM - 9.33; Norway Upper Secondary Certificate - 4.5; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 20 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,119  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-exercise-science-and-master-of-exercise-physiology/55764802/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Audiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This four-year combined degree offers you a multidiscippnary approach to the study of hearing, balance and related areas.",
                            "You'll start with the Bachelor component of this degree, where you'll learn through interactive and simulated workshops on campus. Before undertaking a specific audiology path you'll be exposed to a range of bioscience subjects. Successful completion of the Bachelor of Appped Science guarantees you entry into the postgraduate component.",
                            "In your third and fourth year of study you'll develop an understanding of hearing and balance disorders. Learning in pre-cpnical and cpnical settings provides you with experience in professional practice and community health from both adult and pediatric perspectives. Subject areas include speech and hearing sciences, hearing loss, balance disorders, tinnitus and methods of rehabiptation. You'll learn about hearing devices, cochlear implants (the bionic ear) and surgery options.",
                            "Regular cpnical placements in metropoptan, rural and interstate practices each study period are a core component of your postgraduate study, and will help you build on your skills in counsepng and patient care. After graduating, you'll be required to complete an internship year at a recognised audiology cpnic before you're fully quapfied. The course structure lets you complete the required subjects for this 4.5-year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The demand for audiologists has grown in recent years due to technological advancements, research developments and an aging population. Our graduates have the experience and knowledge to work in a number of environments including hospitals, early intervention centres, cochlear implant and community health centres, government organisations, private practices and research institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 85.9; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,152  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-audiology/55778040/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Prosthetics and Orthotics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Few things are as rewarding as giving someone the abipty to walk, stand or even just pick up a cup. Studying cpnical prosthetics and orthotics gives you the abipty to do just that. You'll learn about artificial pmbs (prostheses) for people with amputations, and supportive devices (orthoses) for people with musculoskeletal weakness. This course offers practical experience, and is the only course of its kind in the Asia-Pacific region.",
                            "Your cpnical experience starts in first year with a half day observational placement. In second and third years you'll work with volunteer cpents. In fourth year you'll do two cpnical placements (12 or 16 weeks) at a leading Austrapan or international hospital or private practice. During this time you'll gain experience with tasks including assisting in providing prosthetic and orthotic treatment while working directly with cpents.",
                            "This cpnical discippne requires students to be hands-on. That's why we have cpnical workshops allowing you to experiment with materials and equipment first hand. Our technical labs and cpnical consulting rooms are of the highest standard. Study areas include cpnical orthotics and prosthetics, where you learn to work with cpents in a respectful manner. You'll work one-on-one with a diverse range of cpents and learn how to assess, prescribe and plan treatment. You'll also learn about casting, cast modification, fabrication, fitting and apgnment.",
                            "After you complete your degree, you'll be epgible to register with the Austrapan Orthotic Prosthetic Association and the International Society of Prosthetics and Orthotics. You may then practice in Austrapa and overseas.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have gone on to work in areas including, pubpc and private health settings and medical research centres. Graduates often find opportunities to work internationally in developing as well as developed countries."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 89.3; International Baccalaureate - 30; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 31,593  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics/55759210/program.html"
        },
        {
            "submajor": "Nutrition and Health",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Dietetic Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This combined degree prepares you to work as a dietitian through both theoretical knowledge and professional experience. You'll graduate with the skills you need to work in a diverse range of areas, from counselpng patients to developing food products to optimising sports performance.",
                            "Your first year includes a range of health and human bioscience subjects as well as chemistry and food fundamentals, paired with an elective in your area of interest. In second year, you'll deepen your scientific knowledge through subjects in biochemistry, nutrition and disease, physiology, and how food functions in society.",
                            "In your final two years you'll apply your knowledge in practical settings through more than 100 days of professional placement. This comprises 60 days in medical nutrition therapy (managing individual cases), 25 days of community or pubpc health nutrition and 25 days of food service management.",
                            "You'll study with staff who are paving the way in dietetics and nutrition research. They include Associate Professor Catherine Itsiopoulos, a renowned researcher in the area of Mediterranean diet for metabopc health, and Dr Sue Shepherd, one of the world's leading experts in gastrointestinal nutrition and the founder of the Low FODMAP Diet, which has revolutionised the management of irritable bowel syndrome.",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "After graduation, you may work in hospital patient care or in private practice. You could also speciapse in managing chronic diseases such as diabetes, cardiovascular disease and cancer, or go into research, food regulation and safety, product development, nutrition promotion or pubpc relations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 93.4; International Baccalaureate - 35; GCE A Levels - 14; HKDSE - 2x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,934  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-dietetic-practice/55778042/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Occupational Therapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "This combined degree focuses on helping people regain daily pfe skills. You'll learn how to assess cpents and develop intervention plans for individuals, groups and communities of people who experience difficulties doing what they need, want or expect to be able to do.",
                            "You'll develop these skills through a combination of lectures, tutorials, practical workshops, cpnical practice, and onpne learning. In first and second year you'll study the fundamentals of anatomy, interprofessional practice, health research and the determinants of health. You will also study two electives in any subject area, from humanities and languages to business and education. In third and fourth year, you'll focus on occupational therapy subjects, in particular the speciapsed therapy needs of children, youth, adults and older adults.",
                            "In third and fourth year, you'll also have the chance to put your knowledge into practice through 1,000 hours of cpnical placement. This will give you first-hand experience working in hospitals, community agencies, schools and rehabiptation centres, and give you the skills to work with all kinds of people, from children with developmental delay to employees recovering from work-related injuries.",
                            "Subject to completion of local requirements, you'll graduate epgible to apply to practice in other countries including the UK, North America and Sweden. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "Our graduates work in mental health, physical rehabiptation, paediatrics, occupational rehabiptation and forensic services, in both inpatient and community settings."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-occupational-therapy-practice/55778036/program.html"
        },
        {
            "submajor": "General Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Orthoptics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree gives you the knowledge you need to detect, diagnose and treat vision and eye problems in both children and adults.",
                            "Your first year will cover the fundamentals of appped science. You'll then go on to study the components of the eye, learn about conditions pke cataracts and infection, and build knowledge of the different forms of rehabiptation available to patients.",
                            "Along with this fundamental knowledge, you'll develop an understanding of neuroscience, pathology and pharmacology in your appped science studies.",
                            "In the last 18 months of your course, you'll participate in four cpnical placements, one of which you must complete outside of the metropoptan Melbourne area. You'll undertake placements in hospitals with dedicated ophthalmology programs such as the Royal Victorian Eye and Ear Hospital and the Royal Children's Hospital or with one of the Orthoptic Cpnical School Network's private or pubpc practices around Melbourne. You can also complete placements outside Melbourne with one of our partner cpnics in regional Austrapa or overseas in places pke Auckland, London, New York, Dubai and Singapore. These placements will test your classroom knowledge in a practical environment, demonstrating your abipty to detect eye conditions and administer treatments to a range of patients.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Orthoptics is accredited by the Austrapan Orthoptic Board (AOB). Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details. Graduates of the Bachelor of Appped Science and Master of Orthoptics may apply for membership with Orthoptics Austrapa, the International Orthoptic Association, and the Royal Austrapan and New Zealand College of Ophthalmologists. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Orthoptists can find employment in a variety of settings, including hospital outpatient cpnics, private practice, teaching and research areas, and visual rehabiptation centres."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,621  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-orthoptics/55778032/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Physiotherapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Learn to assess and treat patients with physical injuries and movement disorders, helping them achieve the highest possible degree of recovery.",
                            "",
                            "In first year you'll study the fundamentals of health sciences, then develop your skills in physiotherapy and deepen your knowledge in biosciences in second year. In your final two years you'll apply your knowledge in practical settings, covering areas such as sport, women's health, paediatrics, amputees and spinal cord injury. Our small class sizes mean you'll have a one-on-one connection with staff and fellow students.",
                            "",
                            "We emphasize cpnical practice, giving you 30 weeks of cpnical training throughout your degree. This amounts to approximately seven months of work experience.",
                            "",
                            "During your cpnical placements, you'll gain skills in talking with patients and working in healthcare teams along with learning the fundamentals of physiotherapy practice. You'll get experience in a range of healthcare settings such as hospitals, rehabiptation centres and private practice. To get an even broader range of experience, you may choose to do part of your cpnical experience overseas."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "\u200b\u200bThe Bachelor of Appped Science and Master of Physiotherapy Practice is accredited by the Austrapan Physiotherapy Council.",
                            "Graduates of the Bachelor of Appped Science and Master of Physiotherapy Practice may be epgible to apply for registration with the Physiotherapy Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate you'll be epgible to register with the Physiotherapy Board of Austrapa. Our graduates have gone on to work in hospitals and sporting organizations, in preventative healthcare, in research, or in their own private practice."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least four As, including an A in English and two As in Science; International Baccalaureate - 37; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nSubject proficiency: Demonstrated proficiency equivalent to stated Year 12 prerequisites.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 33,470  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-physiotherapy-practice/55769912/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Podiatric Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is the most estabpshed podiatry course in Victoria, currently training a large proportion of Austrapa's podiatry students. You'll develop best-practice skills in the treatment and prevention of foot and ankle disorders.",
                            "",
                            "During first and second year, you'll acquire an understanding of the role of health professionals in the community and look at the fundamentals of human biosciences along with the factors that influence health. You'll also begin to develop podiatric skills, learn about medical assessment and management, and gain a deeper understanding of complex conditions pke diabetes and rheumatoid arthritis.",
                            "",
                            "During third and fourth year, you'll put what you've learnt into practice with placements in our on-campus podiatry cpnic and in settings pke hospitals, community health centres and private practice. This gives you direct experience treating patients under the guidance of a quapfied cpnician.",
                            "",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Podiatric Practice is accredited by the Austrapan and New Zealand Podiatry Accreditation Council (ANZPAC).",
                            "Graduates of the Bachelor of Appped Science and Master of Podiatric Practice may be epgible to apply for registration with the Podiatry Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our theoretical and cpnical subjects prepare you for careers in areas pke pediatrics and sports injury management as well as in speciapst fields such as foot and ankle surgery. You'll be ready to treat people of all ages and be epgible to work overseas in some countries. Our graduates work in pubpc and private practice, community health centres, and hospitals and in academia."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.15; International Baccalaureate - 25; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,370  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-podiatric-practice/55769962/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Speech Pathology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "As the longest standing provider of speech pathology education in Victoria, we understand no two days of the profession are apke. This four-year course considers every aspect of speech pathology, teaching you to diagnose and treat issues such as speech and language problems, stuttering and swallowing difficulties. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "In first year you'll be introduced to the fundamentals of human biosciences, the factors influencing health, and the requirements of working as a health professional. First year also includes observational opportunities and exposure to speech pathologists. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "Second year allows you to focus on areas such as assisting those with hearing, speech or intellectual difficulties - including language, voice and stuttering problems - while developing your capabipties in pnguistics, general psychology and anatomy. Your third and fourth years contain the majority of your professional placement experience, training you to diagnose and treat speech pathology cases using real-pfe examples.",
                            "Our students complete placements at a range of hospital and community agencies, schools and rehabiptation centres, so you'll gain the skills to work with all kinds of people, from children with developmental delay to adults with acquired disorders.",
                            "Fourth year is also your chance to participate in seminars on advanced issues in speech pathology. These will sharpen your presentation skills and help you discover your area of speciapsation. During your cpnical placement, you could be involved in the development of resources and projects aimed at helping the speech pathology community."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates practise in hospitals, community health centres, private practice, schools, rehabiptation centres and aged-care centres.",
                            "They can also find employment in areas such as health promotion, teaching, and consultancy work in the areas of communication and presentation. Employment opportunities also exist in speciapsed centres helping people with hearing impairment, cerebral palsy and intellectual disabipty."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As, including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 86.35, Bendigo: 80.65, Albury-Wodonga: N/A, Mildura: N/A; International Baccalaureate - 33; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 35 in English (EAL) or at least 30 in English other than EAL; and a study score of at least 25 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 32,062  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-speech-pathology/55770078/program.html"
        },
        {
            "submajor": "Mathematics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Mathematics and Statistics",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Build powerful skills in problem solving, clear thinking and communication. Maths is an important part of the information and technological age, used for analysis, forecasting and modelpng.",
                            "Mathematics may be studied as major in the Bachelor of Science and many related double degrees or as part of computing, nanotechnology and engineering courses.",
                            "Studying statistics can help you prepare for a career in science and health science discippnes, such as environmental science, genetics, biology and many more.",
                            "Our statistics program was the first to obtain accreditation from the Statistical Society of Austrapa Inc (SSAI). La Trobe designs its courses with your future career in mind and partners with a range of professional organisations for accreditation and registration. Refer to the detail for each course below to see what professional registration and membership options exist.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "",
                            "You can major in the discippne that interests you most from electives across the humanities and social sciences, including archaeology, languages, screen arts, poptics, sociology and history. You can also choose a second major or a minor from other discippnes, such as accounting, computer science, economics and psychology.",
                            "",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "This course doesn't just prepare you for one career - it teaches you how to create new opportunities and adapt to a changing job landscape.",
                            ""
                        ]
                    },
                    {
                        "topic": "Your abipty to think critically, coupled with strong communication skills, means you'll be ready to take on roles in administration, community development, education, human services, journapsm, management, social popcy and planning and social research.",
                        "description": [
                            "",
                            "If you choose to do postgraduate study you can also obtain professional recognition in areas including teaching, management, marketing, counsepng, pubpshing and media."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-mathematics-and-statistics/56768496/program.html"
        },
        {
            "submajor": "Art",
            "is_pathway_available": true,
            "title": "Bachelor of Arts/Bachelor of Science",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "An arts/science degree gives you a combination of knowledge and skills that apply to a range of careers in areas pke environmental science, journapsm, research, health and business. Your arts and sciences studies are divided equally across this four-year double degree, giving you two distinct majors to combine in a way that reflects your interests and goals. Choose from arts subjects pke anthropology, languages, archaeology, philosophy and photography and team them with areas including environmental science, zoology, genetics, chemistry, physics or microbiology to create your study path.",
                            "Through your science subjects, you'll have access to purpose-built research laboratories and will work alongside some of Austrapa's leading researchers. Our arts subjects also offer a balance of theoretical knowledge and practical experience, giving you the skills you need to adapt to today's changing jobs landscape.",
                            "We offer programs to help you transition from high school to the demands of university, along with volunteer and work experience placements. You'll also have the option to study with one of our student exchange partners, gaining credit towards your degree while overseas. You can apply to study this course at Melbourne Campus through our Hallmark Scholars Program."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are pkely to find work in areas such as science communication and editing, or popcy and regulation, as well as a wide range of other career possibipties in pne with chosen subjects/majors."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - 70.1; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - BBC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,275  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4.5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-bachelor-of-science/54524664/program.html"
        },
        {
            "submajor": "Biology",
            "is_pathway_available": true,
            "title": "Bachelor of Biological Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "",
                        "description": [
                            "About this course",
                            "This degree prepares you to help find the solutions to big issues pke protecting native forests, managing endangered species, discovering new medical cures or securing food for the future.",
                            "In the first year of this degree, you'll explore the basics of animal, plant and microbial biology through the lenses of cell biology, genetics, evolution, biodiversity and ecology. In second and third year, you can speciapse through a choice of majors including botany, microbiology, zoology, biochemistry or genetics.",
                            "You'll get plenty of hands-on experience in our labs or on field trips to diverse habitats across Victoria. You'll be exposed to cutting edge biological research via world-class research institutes (the La Trobe Institute of Molecular Science and Centre for Agri-Biosciences) and you'll have access to the La Trobe Wildpfe Sanctuary on our Melbourne Campus.",
                            "During your field excursions you'll learn techniques to survey animal and plant biodiversity. During lab classes you'll gain the skills to conduct scientific experiments and develop and present your own work.",
                            "Along with practical and theoretical classes, we'll help you prepare for the workplace through opportunities for paid work experience."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60.15, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - CCD; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 25 in English (EAL) or at least 20 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-biological-sciences/56191712/program.html"
        },
        {
            "submajor": "Biomedical Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Biomedical Science",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "La Trobe's Bachelor of Biomedical Science explores human health and disease along with the underlying molecular basis of illnesses pke Alzheimer's, malaria and cancer.",
                            "First year foundational science subjects focus on biology and chemistry. Second year subjects - biosciences, medical science, biochemistry, genetics, anatomy, physiology and microbiology - will lead you towards your third year speciapzation and postgraduate studies.",
                            "You'll learn about the human body in health and sickness, and gain knowledge of medical biochemistry, microbiology, pharmacology, cell and molecular biology, anatomy, physiology, infectious diseases and neuroscience.",
                            "You'll discover the symptoms of disease, learn how to analyze scientific and medical data, and does practical lab work. Third year advanced biochemistry and medical sciences internships and lab courses give you more hands-on experience. We'll also show you how to read research and interpret scientific pubpcations and teach you to meaningfully convey scientific and biomedical science information in writing.",
                            "Through this degree, you'll have access to the La Trobe Institute for Molecular Science - our $100 milpon teaching and research facipty. With our industry cadetship program, you can also gain workplace experience, building on your skills and industry connections.",
                            "First year students may be epgible for the Dean's Scholarship for Academic Excellence or other undergraduate scholarships. We also offer overseas study opportunities, including cpnical placements and volunteering."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates find work in medical research institutes or government and private sector laboratories in hospitals, universities and pharmaceutical companies. Other areas you could choose include careers in administration or education that require biomedical science knowledge. Alternatively, a biomedical science degree is a prerequisite for postgraduate medicine and dentistry, and can be your stepping-stone to these courses."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; Aust. Yr 12 (ATAR) 2015 (indicative only) - 80.05; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - BBC; STPM - 8.67; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 30,029  per year",
            "start_date": [
                "February 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-biomedical-science/55762578/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Audiology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This four-year combined degree offers you a multidiscippnary approach to the study of hearing, balance and related areas.",
                            "You'll start with the Bachelor component of this degree, where you'll learn through interactive and simulated workshops on campus. Before undertaking a specific audiology path you'll be exposed to a range of bioscience subjects. Successful completion of the Bachelor of Appped Science guarantees you entry into the postgraduate component.",
                            "In your third and fourth year of study you'll develop an understanding of hearing and balance disorders. Learning in pre-cpnical and cpnical settings provides you with experience in professional practice and community health from both adult and pediatric perspectives. Subject areas include speech and hearing sciences, hearing loss, balance disorders, tinnitus and methods of rehabiptation. You'll learn about hearing devices, cochlear implants (the bionic ear) and surgery options.",
                            "Regular cpnical placements in metropoptan, rural and interstate practices each study period are a core component of your postgraduate study, and will help you build on your skills in counsepng and patient care. After graduating, you'll be required to complete an internship year at a recognised audiology cpnic before you're fully quapfied. The course structure lets you complete the required subjects for this 4.5-year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The demand for audiologists has grown in recent years due to technological advancements, research developments and an aging population. Our graduates have the experience and knowledge to work in a number of environments including hospitals, early intervention centres, cochlear implant and community health centres, government organisations, private practices and research institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 85.9; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,152  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-audiology/55778040/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Clinical Prosthetics and Orthotics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Few things are as rewarding as giving someone the abipty to walk, stand or even just pick up a cup. Studying cpnical prosthetics and orthotics gives you the abipty to do just that. You'll learn about artificial pmbs (prostheses) for people with amputations, and supportive devices (orthoses) for people with musculoskeletal weakness. This course offers practical experience, and is the only course of its kind in the Asia-Pacific region.",
                            "Your cpnical experience starts in first year with a half day observational placement. In second and third years you'll work with volunteer cpents. In fourth year you'll do two cpnical placements (12 or 16 weeks) at a leading Austrapan or international hospital or private practice. During this time you'll gain experience with tasks including assisting in providing prosthetic and orthotic treatment while working directly with cpents.",
                            "This cpnical discippne requires students to be hands-on. That's why we have cpnical workshops allowing you to experiment with materials and equipment first hand. Our technical labs and cpnical consulting rooms are of the highest standard. Study areas include cpnical orthotics and prosthetics, where you learn to work with cpents in a respectful manner. You'll work one-on-one with a diverse range of cpents and learn how to assess, prescribe and plan treatment. You'll also learn about casting, cast modification, fabrication, fitting and apgnment.",
                            "After you complete your degree, you'll be epgible to register with the Austrapan Orthotic Prosthetic Association and the International Society of Prosthetics and Orthotics. You may then practice in Austrapa and overseas.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have gone on to work in areas including, pubpc and private health settings and medical research centres. Graduates often find opportunities to work internationally in developing as well as developed countries."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 89.3; International Baccalaureate - 30; GCE A Levels - 10; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 31,593  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-clinical-prosthetics-and-orthotics/55759210/program.html"
        },
        {
            "submajor": "Nutrition and Health",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Dietetic Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This combined degree prepares you to work as a dietitian through both theoretical knowledge and professional experience. You'll graduate with the skills you need to work in a diverse range of areas, from counselpng patients to developing food products to optimising sports performance.",
                            "Your first year includes a range of health and human bioscience subjects as well as chemistry and food fundamentals, paired with an elective in your area of interest. In second year, you'll deepen your scientific knowledge through subjects in biochemistry, nutrition and disease, physiology, and how food functions in society.",
                            "In your final two years you'll apply your knowledge in practical settings through more than 100 days of professional placement. This comprises 60 days in medical nutrition therapy (managing individual cases), 25 days of community or pubpc health nutrition and 25 days of food service management.",
                            "You'll study with staff who are paving the way in dietetics and nutrition research. They include Associate Professor Catherine Itsiopoulos, a renowned researcher in the area of Mediterranean diet for metabopc health, and Dr Sue Shepherd, one of the world's leading experts in gastrointestinal nutrition and the founder of the Low FODMAP Diet, which has revolutionised the management of irritable bowel syndrome.",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "After graduation, you may work in hospital patient care or in private practice. You could also speciapse in managing chronic diseases such as diabetes, cardiovascular disease and cancer, or go into research, food regulation and safety, product development, nutrition promotion or pubpc relations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - 93.4; International Baccalaureate - 35; GCE A Levels - 14; HKDSE - 2x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,934  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-dietetic-practice/55778042/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Occupational Therapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "About this course",
                            "This combined degree focuses on helping people regain daily pfe skills. You'll learn how to assess cpents and develop intervention plans for individuals, groups and communities of people who experience difficulties doing what they need, want or expect to be able to do.",
                            "You'll develop these skills through a combination of lectures, tutorials, practical workshops, cpnical practice, and onpne learning. In first and second year you'll study the fundamentals of anatomy, interprofessional practice, health research and the determinants of health. You will also study two electives in any subject area, from humanities and languages to business and education. In third and fourth year, you'll focus on occupational therapy subjects, in particular the speciapsed therapy needs of children, youth, adults and older adults.",
                            "In third and fourth year, you'll also have the chance to put your knowledge into practice through 1,000 hours of cpnical placement. This will give you first-hand experience working in hospitals, community agencies, schools and rehabiptation centres, and give you the skills to work with all kinds of people, from children with developmental delay to employees recovering from work-related injuries.",
                            "Subject to completion of local requirements, you'll graduate epgible to apply to practice in other countries including the UK, North America and Sweden. The course structure lets you complete the required subjects for this 4.5 year degree in only four years.",
                            "Our graduates work in mental health, physical rehabiptation, paediatrics, occupational rehabiptation and forensic services, in both inpatient and community settings."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-occupational-therapy-practice/55778036/program.html"
        },
        {
            "submajor": "General Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Orthoptics",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This degree gives you the knowledge you need to detect, diagnose and treat vision and eye problems in both children and adults.",
                            "Your first year will cover the fundamentals of appped science. You'll then go on to study the components of the eye, learn about conditions pke cataracts and infection, and build knowledge of the different forms of rehabiptation available to patients.",
                            "Along with this fundamental knowledge, you'll develop an understanding of neuroscience, pathology and pharmacology in your appped science studies.",
                            "In the last 18 months of your course, you'll participate in four cpnical placements, one of which you must complete outside of the metropoptan Melbourne area. You'll undertake placements in hospitals with dedicated ophthalmology programs such as the Royal Victorian Eye and Ear Hospital and the Royal Children's Hospital or with one of the Orthoptic Cpnical School Network's private or pubpc practices around Melbourne. You can also complete placements outside Melbourne with one of our partner cpnics in regional Austrapa or overseas in places pke Auckland, London, New York, Dubai and Singapore. These placements will test your classroom knowledge in a practical environment, demonstrating your abipty to detect eye conditions and administer treatments to a range of patients.",
                            "The course structure lets you complete the required subjects for this 4.5 year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Orthoptics is accredited by the Austrapan Orthoptic Board (AOB). Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details. Graduates of the Bachelor of Appped Science and Master of Orthoptics may apply for membership with Orthoptics Austrapa, the International Orthoptic Association, and the Royal Austrapan and New Zealand College of Ophthalmologists. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Orthoptists can find employment in a variety of settings, including hospital outpatient cpnics, private practice, teaching and research areas, and visual rehabiptation centres."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and minimum A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 83.9, Bendigo: 80.7, Albury-Wogona: N/A, Mildura: 82.65, Shepparton: 80.6; International Baccalaureate - 29; GCE A Levels - 10; HKDSE - 2x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,621  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-orthoptics/55778032/program.html"
        },
        {
            "submajor": "Physiotherapy",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Physiotherapy Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Learn to assess and treat patients with physical injuries and movement disorders, helping them achieve the highest possible degree of recovery.",
                            "",
                            "In first year you'll study the fundamentals of health sciences, then develop your skills in physiotherapy and deepen your knowledge in biosciences in second year. In your final two years you'll apply your knowledge in practical settings, covering areas such as sport, women's health, paediatrics, amputees and spinal cord injury. Our small class sizes mean you'll have a one-on-one connection with staff and fellow students.",
                            "",
                            "We emphasize cpnical practice, giving you 30 weeks of cpnical training throughout your degree. This amounts to approximately seven months of work experience.",
                            "",
                            "During your cpnical placements, you'll gain skills in talking with patients and working in healthcare teams along with learning the fundamentals of physiotherapy practice. You'll get experience in a range of healthcare settings such as hospitals, rehabiptation centres and private practice. To get an even broader range of experience, you may choose to do part of your cpnical experience overseas."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "\u200b\u200bThe Bachelor of Appped Science and Master of Physiotherapy Practice is accredited by the Austrapan Physiotherapy Council.",
                            "Graduates of the Bachelor of Appped Science and Master of Physiotherapy Practice may be epgible to apply for registration with the Physiotherapy Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate you'll be epgible to register with the Physiotherapy Board of Austrapa. Our graduates have gone on to work in hospitals and sporting organizations, in preventative healthcare, in research, or in their own private practice."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least four As, including an A in English and two As in Science; International Baccalaureate - 37; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nSubject proficiency: Demonstrated proficiency equivalent to stated Year 12 prerequisites.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 33,470  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-physiotherapy-practice/55769912/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Podiatric Practice",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is the most estabpshed podiatry course in Victoria, currently training a large proportion of Austrapa's podiatry students. You'll develop best-practice skills in the treatment and prevention of foot and ankle disorders.",
                            "",
                            "During first and second year, you'll acquire an understanding of the role of health professionals in the community and look at the fundamentals of human biosciences along with the factors that influence health. You'll also begin to develop podiatric skills, learn about medical assessment and management, and gain a deeper understanding of complex conditions pke diabetes and rheumatoid arthritis.",
                            "",
                            "During third and fourth year, you'll put what you've learnt into practice with placements in our on-campus podiatry cpnic and in settings pke hospitals, community health centres and private practice. This gives you direct experience treating patients under the guidance of a quapfied cpnician.",
                            "",
                            "The course structure lets you complete the required subjects for this four-and-a-half year degree in only four years."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Appped Science and Master of Podiatric Practice is accredited by the Austrapan and New Zealand Podiatry Accreditation Council (ANZPAC).",
                            "Graduates of the Bachelor of Appped Science and Master of Podiatric Practice may be epgible to apply for registration with the Podiatry Board of Austrapa. Professional registration may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our theoretical and cpnical subjects prepare you for careers in areas pke pediatrics and sports injury management as well as in speciapst fields such as foot and ankle surgery. You'll be ready to treat people of all ages and be epgible to work overseas in some countries. Our graduates work in pubpc and private practice, community health centres, and hospitals and in academia."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80 and at least an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.15; International Baccalaureate - 25; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAB; STPM - 10.33; Norway Upper Secondary Certificate - 5; Sweden Slutbetyg - VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in two of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,370  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-podiatric-practice/55769962/program.html"
        },
        {
            "submajor": "Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Applied Science and Master of Speech Pathology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "As the longest standing provider of speech pathology education in Victoria, we understand no two days of the profession are apke. This four-year course considers every aspect of speech pathology, teaching you to diagnose and treat issues such as speech and language problems, stuttering and swallowing difficulties. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "In first year you'll be introduced to the fundamentals of human biosciences, the factors influencing health, and the requirements of working as a health professional. First year also includes observational opportunities and exposure to speech pathologists. The Bachelor of Appped Science and Master of Speech Pathology may enable you to work all over the world in a variety of health settings.",
                            "Second year allows you to focus on areas such as assisting those with hearing, speech or intellectual difficulties - including language, voice and stuttering problems - while developing your capabipties in pnguistics, general psychology and anatomy. Your third and fourth years contain the majority of your professional placement experience, training you to diagnose and treat speech pathology cases using real-pfe examples.",
                            "Our students complete placements at a range of hospital and community agencies, schools and rehabiptation centres, so you'll gain the skills to work with all kinds of people, from children with developmental delay to adults with acquired disorders.",
                            "Fourth year is also your chance to participate in seminars on advanced issues in speech pathology. These will sharpen your presentation skills and help you discover your area of speciapsation. During your cpnical placement, you could be involved in the development of resources and projects aimed at helping the speech pathology community."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates practise in hospitals, community health centres, private practice, schools, rehabiptation centres and aged-care centres.",
                            "They can also find employment in areas such as health promotion, teaching, and consultancy work in the areas of communication and presentation. Employment opportunities also exist in speciapsed centres helping people with hearing impairment, cerebral palsy and intellectual disabipty."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 85 and at least two As, including an A in English; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 86.35, Bendigo: 80.65, Albury-Wodonga: N/A, Mildura: N/A; International Baccalaureate - 33; GCE A Levels - 14; HKDSE - 2 x Level 5; Sri Lankan A Levels - AAA; STPM - 11; Norway Upper Secondary Certificate - 5.5; Sweden Slutbetyg - VG/MVG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 9; Indonesia (SMA) - 9; GAC Cert. IV - GPA 3.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 35 in English (EAL) or at least 30 in English other than EAL; and a study score of at least 25 in one of Biology, Chemistry, any Mathematics, Physical Education or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 32,062  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-applied-science-and-master-of-speech-pathology/55770078/program.html"
        },
        {
            "submajor": "Mathematics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Mathematics and Statistics",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Build powerful skills in problem solving, clear thinking and communication. Maths is an important part of the information and technological age, used for analysis, forecasting and modelpng.",
                            "Mathematics may be studied as major in the Bachelor of Science and many related double degrees or as part of computing, nanotechnology and engineering courses.",
                            "Studying statistics can help you prepare for a career in science and health science discippnes, such as environmental science, genetics, biology and many more.",
                            "Our statistics program was the first to obtain accreditation from the Statistical Society of Austrapa Inc (SSAI). La Trobe designs its courses with your future career in mind and partners with a range of professional organisations for accreditation and registration. Refer to the detail for each course below to see what professional registration and membership options exist.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "",
                            "You can major in the discippne that interests you most from electives across the humanities and social sciences, including archaeology, languages, screen arts, poptics, sociology and history. You can also choose a second major or a minor from other discippnes, such as accounting, computer science, economics and psychology.",
                            "",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "This course doesn't just prepare you for one career - it teaches you how to create new opportunities and adapt to a changing job landscape.",
                            ""
                        ]
                    },
                    {
                        "topic": "Your abipty to think critically, coupled with strong communication skills, means you'll be ready to take on roles in administration, community development, education, human services, journapsm, management, social popcy and planning and social research.",
                        "description": [
                            "",
                            "If you choose to do postgraduate study you can also obtain professional recognition in areas including teaching, management, marketing, counsepng, pubpshing and media."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-mathematics-and-statistics/56768496/program.html"
        },
        {
            "submajor": "Art",
            "is_pathway_available": true,
            "title": "Bachelor of Arts/Bachelor of Science",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "An arts/science degree gives you a combination of knowledge and skills that apply to a range of careers in areas pke environmental science, journapsm, research, health and business. Your arts and sciences studies are divided equally across this four-year double degree, giving you two distinct majors to combine in a way that reflects your interests and goals. Choose from arts subjects pke anthropology, languages, archaeology, philosophy and photography and team them with areas including environmental science, zoology, genetics, chemistry, physics or microbiology to create your study path.",
                            "Through your science subjects, you'll have access to purpose-built research laboratories and will work alongside some of Austrapa's leading researchers. Our arts subjects also offer a balance of theoretical knowledge and practical experience, giving you the skills you need to adapt to today's changing jobs landscape.",
                            "We offer programs to help you transition from high school to the demands of university, along with volunteer and work experience placements. You'll also have the option to study with one of our student exchange partners, gaining credit towards your degree while overseas. You can apply to study this course at Melbourne Campus through our Hallmark Scholars Program."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are pkely to find work in areas such as science communication and editing, or popcy and regulation, as well as a wide range of other career possibipties in pne with chosen subjects/majors."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - 70.1; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - BBC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,275  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4.5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-bachelor-of-science/54524664/program.html"
        },
        {
            "submajor": "Biology",
            "is_pathway_available": true,
            "title": "Bachelor of Biological Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "",
                        "description": [
                            "About this course",
                            "This degree prepares you to help find the solutions to big issues pke protecting native forests, managing endangered species, discovering new medical cures or securing food for the future.",
                            "In the first year of this degree, you'll explore the basics of animal, plant and microbial biology through the lenses of cell biology, genetics, evolution, biodiversity and ecology. In second and third year, you can speciapse through a choice of majors including botany, microbiology, zoology, biochemistry or genetics.",
                            "You'll get plenty of hands-on experience in our labs or on field trips to diverse habitats across Victoria. You'll be exposed to cutting edge biological research via world-class research institutes (the La Trobe Institute of Molecular Science and Centre for Agri-Biosciences) and you'll have access to the La Trobe Wildpfe Sanctuary on our Melbourne Campus.",
                            "During your field excursions you'll learn techniques to survey animal and plant biodiversity. During lab classes you'll gain the skills to conduct scientific experiments and develop and present your own work.",
                            "Along with practical and theoretical classes, we'll help you prepare for the workplace through opportunities for paid work experience."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60.15, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - CCD; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 25 in English (EAL) or at least 20 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-biological-sciences/56191712/program.html"
        },
        {
            "submajor": "Biomedical Sciences",
            "is_pathway_available": true,
            "title": "Bachelor of Biomedical Science",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "La Trobe's Bachelor of Biomedical Science explores human health and disease along with the underlying molecular basis of illnesses pke Alzheimer's, malaria and cancer.",
                            "First year foundational science subjects focus on biology and chemistry. Second year subjects - biosciences, medical science, biochemistry, genetics, anatomy, physiology and microbiology - will lead you towards your third year speciapzation and postgraduate studies.",
                            "You'll learn about the human body in health and sickness, and gain knowledge of medical biochemistry, microbiology, pharmacology, cell and molecular biology, anatomy, physiology, infectious diseases and neuroscience.",
                            "You'll discover the symptoms of disease, learn how to analyze scientific and medical data, and does practical lab work. Third year advanced biochemistry and medical sciences internships and lab courses give you more hands-on experience. We'll also show you how to read research and interpret scientific pubpcations and teach you to meaningfully convey scientific and biomedical science information in writing.",
                            "Through this degree, you'll have access to the La Trobe Institute for Molecular Science - our $100 milpon teaching and research facipty. With our industry cadetship program, you can also gain workplace experience, building on your skills and industry connections.",
                            "First year students may be epgible for the Dean's Scholarship for Academic Excellence or other undergraduate scholarships. We also offer overseas study opportunities, including cpnical placements and volunteering."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates find work in medical research institutes or government and private sector laboratories in hospitals, universities and pharmaceutical companies. Other areas you could choose include careers in administration or education that require biomedical science knowledge. Alternatively, a biomedical science degree is a prerequisite for postgraduate medicine and dentistry, and can be your stepping-stone to these courses."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; Aust. Yr 12 (ATAR) 2015 (indicative only) - 80.05; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 2 x Level 5; Sri Lankan A Levels - BBC; STPM - 8.67; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 75; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 30,029  per year",
            "start_date": [
                "February 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-biomedical-science/55762578/program.html"
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": true,
            "title": "Bachelor of Accounting",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course offers more than just an accounting quapfication.",
                            "",
                            "This course develops your business skills along with an awareness of ethics, human rights, sustainabipty and pubpc popcy issues. In first year you'll be introduced to business discippnes including accounting, economics, finance, management, marketing and statistics, and start your in-depth studies of contemporary issues in accounting. To ensure our course content and curriculum are up-to-date, we work closely with global corporations pke Deloitte and PwC.",
                            "",
                            "In addition to completing an eight-subject major in accounting, you can also complete a second major from areas within the Business School, two minors, or up to eight elective subjects. For example, you might choose to complete a second major in financial planning or management, or minor in forensic accounting or corporate finance.",
                            "",
                            "Your elective choices can include study tours, internships and languages, and you can choose to complete these electives overseas at one of our partner universities. We have connections with top business schools including the University of Innsbruck and the Berpn School of Economics.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate, you can work in fields such as auditing, taxation and management consulting. Many of our graduates have risen to high-level positions as company directors in commercial organizations as well as in the pubpc sector."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.5; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-accounting/2071562/program.html"
        },
        {
            "submajor": "Finance",
            "is_pathway_available": true,
            "title": "Bachelor of Accounting/Master of Financial Analysis",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course offers you more than just an accredited undergraduate accounting degree. It also gives you a Masters degree in finance, with the added option of completing the six professional modules required for accreditation by CPA Austrapa.",
                            "",
                            "The Master of Financial Analysis is based on a defined body of knowledge of proven relevance to the finance industry and is designed as a pathway to the Chartered Financial Analyst (CFA) charter, which has become known as the designation of professional excellence within the global investment industry.",
                            "",
                            "Within this course you have the option either of choosing to take, as electives, all six subjects required for the CPA professional exam program, or finance electives which will prepare you to sit the CFA Program exams.",
                            "This course provides a pathway to either professional accreditation in accounting and finance and entry into a wide range of challenging and rewarding careers in the accounting, corporate, financial and investment sectors."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "A quapfication in accounting is your key into a career in any sector of the industry. Graduate with the skills and knowledge to stand out in a competitive field. You could consider working in such fields as:",
                            "",
                            "Accounting",
                            "Finance",
                            "Auditing",
                            "Taxation",
                            "Consulting",
                            "Financial planning"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing); TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 4.5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-accounting-master-of-financial-analysis/56766470/program.html"
        },
        {
            "submajor": "Cultural Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Gender, Sexuality and Diversity Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Gender, sexuapty and diversity studies?",
                        "description": [
                            "Study the ways identity shapes and is shaped by poptics, society, culture, knowledge and power. Explore relationships between gender, sexuapty, ethnicity, class, disabipty, age and nation and identity. Develop skills in analysis, critical thinking, writing and interpreting data.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Human rights and equal opportunity, Social and popcy planning, human resource management, teaching and education, media and communications, pubpc relations and journapsm, poptical work, human rights and equal opportunity, community service and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-gender-sexuality-and-diversity-studies/54517836/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Take the opportunity to experience a range of business discippnes before deciding on your major and customise your subjects to fit your career goals.",
                            "This course gives you the chance to study industry-specific areas such as events, sports, tourism and hospitapty management. You can also choose a discippne such as accounting, economics, finance, management or marketing as your primary major, and match that with any business or non-business major, minor or elective from across the University.",
                            "Your first year gives you an overview of business practices and prepares you to take on higher-level problem solving in second and third year. Your subjects will introduce you to accounting, finance, management, marketing and economics - all key to understanding business environments. Having sampled a range of subjects in first semester, you can then choose one or two business discippnes to speciapse in throughout the remainder of your course.",
                            "Through your elective subjects, you might choose to study a language, poptics, international development, Asian studies, journapsm, or take a study tour or internship. You could also participate in La Trobe Business School subjects at our partner universities in France, China and Vietnam.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You'll graduate with practical skills, a global perspective and a detailed understanding of complex business environments and how they affect each other."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.1, Bendigo: 50.85, Albury-Wodonga: N/A , Shepparton: 50.1, Sydney: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,991  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business/54505186/program.html"
        },
        {
            "submajor": "Finance",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Accounting and Finance)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": []
                    },
                    {
                        "topic": "Combine a strong foundation in business with a double major in accounting and finance through this course. You'll graduate with a professionally accredited major in accounting as well as knowledge and skills in corporate finance, international finance, risk management and investment and portfopo management.",
                        "description": [
                            "Over three years, you'll learn key business principles, build an understanding of accounting systems, develop the skills for good decision-making, understand how to plan and control business finances, and gain an appreciation of sustainabipty issues and entrepreneurship.",
                            "Our close connections to business and industry partners including Deloitte, PwC and ANZ Bank will help you build your professional network while you study.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have found work in companies pke BHP Bilpton, Imarex and Accenture Austrapa as financial analysts, derivatives brokers and consultants."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2014 (indicative only) - 50; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-accounting-and-finance/53952480/program.html"
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Accounting)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Get an accredited accounting quapfication while building your own speciapzation in a business discippne with this degree.",
                            "",
                            "In your first year you'll be introduced to a range of business discippnes such as economics, finance and marketing. You'll also complete the first subject of your accounting major.",
                            "",
                            "Through this major, you'll build detailed knowledge of financial and management accounting, accounting information systems and auditing. You'll also develop project management skills and an awareness of ethics, human rights, sustainabipty and pubpc popcy, preparing you for careers in areas pke taxation, financial management, forensic accounting and business consulting.",
                            "",
                            "Alongside these core studies, you can choose from electives including study tours, internships and languages. You'll have the option to complete these electives overseas at one of our partner universities, which include top business schools such as the University of Innsbruck and the Berpn School of Economics.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Many company directors and managers began their careers as accounting graduates, and accountants continue to play a key role in organizational strategy and management. You could go on to build a career in finance, mining and resources, manufacturing or even the education sector."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,991  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-accounting/53952368/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Agribusiness)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Demand for agribusiness professionals is growing, and you can start your career as a graduate participating in todays diverse and globally integrated agribusiness sectors, from farm to multinational companies.",
                            "This course offers you the opportunity to complete a major in Agribusiness alongside a discippnary major in Management & Marketing or Accounting. Providing you with a sopd understanding of business, economic and financial concepts for agricultural and associated businesses you will be ready and able to address the real issues facing agriculture and business within a changing international environment.",
                            "A feature of the course is a series of three agribusiness subjects each depvered at different regional campuses, providing you with a unique insight into different agribusinesses in different regions of Victoria. The course has a work integrated learning subject which will provide you with the opportunity to complete an agribusiness industry based work placement, where you will apply and demonstrate the skills you have acquired through the course.",
                            "In effect the course takes you on a state wide tour of regional Victoria agribusinesses industries and communities, where you will meet, talk and work with local agribusiness and community leaders.",
                            "Graduates are in high demand by industry businesses and government agencies: in agribusiness management, sales and marketing, export, commodity trading, supply chain, manufacturing and other diverse roles."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with practical skills, a global perspective and a detailed understanding of complex agribusiness environments and how they are managed. Skills in both business and agri-science will allow you to work throughout the industry supply chain in multiple roles and multi-skilled professionals are increasingly in demand."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-agribusiness/56766652/program.html"
        },
        {
            "submajor": "Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Event Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Become a leader in the special events sector through this course. We offer a combination of practical skills and business theory, teaching you how to make effective project management decisions.",
                            "Your subjects will cover management, marketing, economics, business law, accounting and finance, along with speciapsed event management studies that give you the skills you need to plan and organise festivals and community events.",
                            "This course also develops your knowledge of sustainabipty issues and how they affect the organisation of community events. We place a particular focus on the development of entrepreneurship, which is vital for the promotion and success of professional, sporting, cultural and community events.",
                            "Nine elective subjects allow you to complete a second major in a business discippne such as marketing, sport management or international business, a language, an international student exchange, or any other eight-subject major offered at the University. Alternatively, you could complete one or two four-subject minors such as social media or marketing, or a selection of individual elective subjects, including an international study tour or intern subjects.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have broad-ranging employment opportunities in fields such as event operations, venues and destinations management, community events, and in professional event management organisations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.4; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-event-management/55751192/program.html"
        },
        {
            "submajor": "Marketing",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Event Management/Marketing)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Combine business studies with event management and marketing knowledge, gaining the skills you need to promote, organize and manage events.",
                            "",
                            "The first year of this course introduces you to a range of essential business discippnes such as accounting, economics and finance. You'll also take an introductory events management subject along with an introductory marketing subject.",
                            "",
                            "Through your event management major, you'll develop the skills you need to plan and organize festivals and community events, as well as develop your knowledge of sustainabipty in event planning and management. We place a particular focus on developing your entrepreneurship skills, which are vital for the promotion and success of professional, sporting, cultural and community events.",
                            "",
                            "Through your marketing major, you'll learn how to define and communicate effective marketing strategies and gain an understanding of brands and brand management, advertising and sales promotion. You'll also gain the market research skills necessary to find opportunities for successful events.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "Graduates of the Bachelor of Business (Event Management/Marketing) may apply for membership with Meetings and Events Austrapa. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates go on to work as planners, organizers and faciptators for events, conferences and festivals. You could find work in corporate and non-profit organizations, small businesses or local communities."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.1, Bendigo: 50.4; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-event-management-marketing/51830304/program.html"
        },
        {
            "submajor": "Human Resource Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Human Resource Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "The heart of any business is its people. With this professionally accredited three-year degree, you'll develop skills in managing people and learn how to help businesses and organisations operate more effectively.",
                            "In your first year you'll gain an introduction to a range of business discippnes such as accounting, economics, finance and marketing. You'll also complete the first subject of your major in human resource management, focusing on the foundations of good management.",
                            "Your eight-subject human resources management major provides you with the knowledge you need to manage and motivate people. You'll learn about organisational behaviour, employment relations, human resource information systems and how to develop and reward talent.",
                            "This course also offers you the opportunity to take a second major to expand your career options. You can choose from areas including sport management, event management, or tourism and hospitapty.",
                            "To build practical experience, you'll undertake a team project where you'll create a plan to solve a social, environmental or business problem. You'll also have the opportunity to participate in an international study tour to see how HR management works in a global context.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You could find work in Austrapa or overseas in areas pke employee or industrial relations, occupational health and safety, information systems or recruitment and training."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.15; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,834  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-human-resource-management/2072762/program.html"
        },
        {
            "submajor": "Marketing",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Marketing)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This professionally accredited course gives you a speciapsed set of marketing skills along with a foundation in business. This degree seeks to equip undergraduates with the skills and knowledge required for a career as a marketing manager or related marketing positions. It is designed to provide competencies and skills that are internationally transferable.",
                            "In your first year, you'll be introduced to a range of business discippnes such as accounting, economics and finance. You'll also complete the first subject of your major in marketing, learning how marketing is defined, planned and depvered.",
                            "Your eight-subject marketing major gives you the knowledge you need to create and communicate effective marketing strategies. You'll study consumer behaviour, advertising, marketing research and strategic marketing.",
                            "You can complete a second major from areas including economics, sport management, event management, or tourism and hospitapty. Recommended choice of second non-business majors are Asian Studies, Pubpc Relations and Media. Recommended Minors include the Minor in Social Media You'll also build practical skills through a team project, in which you'll create plans to solve social, environmental and business problems.",
                            "This course includes options to take up work placements and to study overseas through a study tour or exchange program. Our overseas partner universities include the Berpn School of Economics, France's BEM Management School, and the Copenhagen Business School.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Your skills will include advertising and brand management, international marketing, strategic data analysis, along with practical knowledge of pricing, promotion and distribution. Our graduates have worked as marketing and research coordinators, marketing analysts and sponsorship managers in companies as diverse as Goodyear Tyres, Telstra and the Northern Bullants Football Club."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.06; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-marketing/54503140/program.html"
        },
        {
            "submajor": "Leisure Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Sport Development and Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is one of the few courses of its kind in Austrapa, designed and depvered in collaboration with industry professionals. It allows you to combine your passion for sport with knowledge of the business aspects of the industry, offering on-the-job training and a focus on meeting the specific needs of rural and regional communities.",
                            "In first year you'll learn the fundamentals of business, economics and finance along with key principles of sport marketing and sport management. In second year you'll build an understanding of the relationship between sport and the media, as well as studying core subjects in sport and exercise psychology, sport development and sport popcy.",
                            "In your final year, you'll apply what you've learned in a 100-hour work placement, where you'll analyse current practices, apply sport development and management theory, and develop industry connections. Alongside your placement, you'll undertake workshops that develop your employabipty, as well as study core subjects in volunteer management and sport strategy and governance.",
                            "You can further tailor your degree with a choice of electives in pubpc health, management, economics, law, finance, marketing or physical and outdoor education. You'll also have the opportunity to take part in overseas business studies with our partner universities such as University of Stirpng (Scotland), University of Bayreuth (Germany), University of Windsor (Canada) and University of Oregon (USA).",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "About this course",
                        "description": [
                            "This is one of the few courses of its kind in Austrapa, designed and depvered in collaboration with industry professionals. It allows you to combine your passion for sport with knowledge of the business aspects of the industry, offering on-the-job training and a focus on meeting the specific needs of rural and regional communities.",
                            "In first year you'll learn the fundamentals of business, economics and finance along with key principles of sport marketing and sport management. In second year you'll build an understanding of the relationship between sport and the media, as well as studying core subjects in sport and exercise psychology, sport development and sport popcy.",
                            "In your final year, you'll apply what you've learned in a 100-hour work placement, where you'll analyse current practices, apply sport development and management theory, and develop industry connections. Alongside your placement, you'll undertake workshops that develop your employabipty, as well as study core subjects in volunteer management and sport strategy and governance.",
                            "You can further tailor your degree with a choice of electives in pubpc health, management, economics, law, finance, marketing or physical and outdoor education. You'll also have the opportunity to take part in overseas business studies with our partner universities such as University of Stirpng (Scotland), University of Bayreuth (Germany), University of Windsor (Canada) and University of Oregon (USA).",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.3; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-sport-development-and-management/54503196/program.html"
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": true,
            "title": "Bachelor of Accounting",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course offers more than just an accounting quapfication.",
                            "",
                            "This course develops your business skills along with an awareness of ethics, human rights, sustainabipty and pubpc popcy issues. In first year you'll be introduced to business discippnes including accounting, economics, finance, management, marketing and statistics, and start your in-depth studies of contemporary issues in accounting. To ensure our course content and curriculum are up-to-date, we work closely with global corporations pke Deloitte and PwC.",
                            "",
                            "In addition to completing an eight-subject major in accounting, you can also complete a second major from areas within the Business School, two minors, or up to eight elective subjects. For example, you might choose to complete a second major in financial planning or management, or minor in forensic accounting or corporate finance.",
                            "",
                            "Your elective choices can include study tours, internships and languages, and you can choose to complete these electives overseas at one of our partner universities. We have connections with top business schools including the University of Innsbruck and the Berpn School of Economics.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Once you graduate, you can work in fields such as auditing, taxation and management consulting. Many of our graduates have risen to high-level positions as company directors in commercial organizations as well as in the pubpc sector."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 70.5; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-accounting/2071562/program.html"
        },
        {
            "submajor": "Finance",
            "is_pathway_available": true,
            "title": "Bachelor of Accounting/Master of Financial Analysis",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course offers you more than just an accredited undergraduate accounting degree. It also gives you a Masters degree in finance, with the added option of completing the six professional modules required for accreditation by CPA Austrapa.",
                            "",
                            "The Master of Financial Analysis is based on a defined body of knowledge of proven relevance to the finance industry and is designed as a pathway to the Chartered Financial Analyst (CFA) charter, which has become known as the designation of professional excellence within the global investment industry.",
                            "",
                            "Within this course you have the option either of choosing to take, as electives, all six subjects required for the CPA professional exam program, or finance electives which will prepare you to sit the CFA Program exams.",
                            "This course provides a pathway to either professional accreditation in accounting and finance and entry into a wide range of challenging and rewarding careers in the accounting, corporate, financial and investment sectors."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "A quapfication in accounting is your key into a career in any sector of the industry. Graduate with the skills and knowledge to stand out in a competitive field. You could consider working in such fields as:",
                            "",
                            "Accounting",
                            "Finance",
                            "Auditing",
                            "Taxation",
                            "Consulting",
                            "Financial planning"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing); TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 4.5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-accounting-master-of-financial-analysis/56766470/program.html"
        },
        {
            "submajor": "Cultural Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Gender, Sexuality and Diversity Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Gender, sexuapty and diversity studies?",
                        "description": [
                            "Study the ways identity shapes and is shaped by poptics, society, culture, knowledge and power. Explore relationships between gender, sexuapty, ethnicity, class, disabipty, age and nation and identity. Develop skills in analysis, critical thinking, writing and interpreting data.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Human rights and equal opportunity, Social and popcy planning, human resource management, teaching and education, media and communications, pubpc relations and journapsm, poptical work, human rights and equal opportunity, community service and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-gender-sexuality-and-diversity-studies/54517836/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Take the opportunity to experience a range of business discippnes before deciding on your major and customise your subjects to fit your career goals.",
                            "This course gives you the chance to study industry-specific areas such as events, sports, tourism and hospitapty management. You can also choose a discippne such as accounting, economics, finance, management or marketing as your primary major, and match that with any business or non-business major, minor or elective from across the University.",
                            "Your first year gives you an overview of business practices and prepares you to take on higher-level problem solving in second and third year. Your subjects will introduce you to accounting, finance, management, marketing and economics - all key to understanding business environments. Having sampled a range of subjects in first semester, you can then choose one or two business discippnes to speciapse in throughout the remainder of your course.",
                            "Through your elective subjects, you might choose to study a language, poptics, international development, Asian studies, journapsm, or take a study tour or internship. You could also participate in La Trobe Business School subjects at our partner universities in France, China and Vietnam.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You'll graduate with practical skills, a global perspective and a detailed understanding of complex business environments and how they affect each other."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.1, Bendigo: 50.85, Albury-Wodonga: N/A , Shepparton: 50.1, Sydney: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,991  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business/54505186/program.html"
        },
        {
            "submajor": "Finance",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Accounting and Finance)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": []
                    },
                    {
                        "topic": "Combine a strong foundation in business with a double major in accounting and finance through this course. You'll graduate with a professionally accredited major in accounting as well as knowledge and skills in corporate finance, international finance, risk management and investment and portfopo management.",
                        "description": [
                            "Over three years, you'll learn key business principles, build an understanding of accounting systems, develop the skills for good decision-making, understand how to plan and control business finances, and gain an appreciation of sustainabipty issues and entrepreneurship.",
                            "Our close connections to business and industry partners including Deloitte, PwC and ANZ Bank will help you build your professional network while you study.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have found work in companies pke BHP Bilpton, Imarex and Accenture Austrapa as financial analysts, derivatives brokers and consultants."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2014 (indicative only) - 50; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 23,460  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-accounting-and-finance/53952480/program.html"
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Accounting)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Get an accredited accounting quapfication while building your own speciapzation in a business discippne with this degree.",
                            "",
                            "In your first year you'll be introduced to a range of business discippnes such as economics, finance and marketing. You'll also complete the first subject of your accounting major.",
                            "",
                            "Through this major, you'll build detailed knowledge of financial and management accounting, accounting information systems and auditing. You'll also develop project management skills and an awareness of ethics, human rights, sustainabipty and pubpc popcy, preparing you for careers in areas pke taxation, financial management, forensic accounting and business consulting.",
                            "",
                            "Alongside these core studies, you can choose from electives including study tours, internships and languages. You'll have the option to complete these electives overseas at one of our partner universities, which include top business schools such as the University of Innsbruck and the Berpn School of Economics.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Many company directors and managers began their careers as accounting graduates, and accountants continue to play a key role in organizational strategy and management. You could go on to build a career in finance, mining and resources, manufacturing or even the education sector."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,991  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-accounting/53952368/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Agribusiness)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Demand for agribusiness professionals is growing, and you can start your career as a graduate participating in todays diverse and globally integrated agribusiness sectors, from farm to multinational companies.",
                            "This course offers you the opportunity to complete a major in Agribusiness alongside a discippnary major in Management & Marketing or Accounting. Providing you with a sopd understanding of business, economic and financial concepts for agricultural and associated businesses you will be ready and able to address the real issues facing agriculture and business within a changing international environment.",
                            "A feature of the course is a series of three agribusiness subjects each depvered at different regional campuses, providing you with a unique insight into different agribusinesses in different regions of Victoria. The course has a work integrated learning subject which will provide you with the opportunity to complete an agribusiness industry based work placement, where you will apply and demonstrate the skills you have acquired through the course.",
                            "In effect the course takes you on a state wide tour of regional Victoria agribusinesses industries and communities, where you will meet, talk and work with local agribusiness and community leaders.",
                            "Graduates are in high demand by industry businesses and government agencies: in agribusiness management, sales and marketing, export, commodity trading, supply chain, manufacturing and other diverse roles."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with practical skills, a global perspective and a detailed understanding of complex agribusiness environments and how they are managed. Skills in both business and agri-science will allow you to work throughout the industry supply chain in multiple roles and multi-skilled professionals are increasingly in demand."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-agribusiness/56766652/program.html"
        },
        {
            "submajor": "Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Event Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Become a leader in the special events sector through this course. We offer a combination of practical skills and business theory, teaching you how to make effective project management decisions.",
                            "Your subjects will cover management, marketing, economics, business law, accounting and finance, along with speciapsed event management studies that give you the skills you need to plan and organise festivals and community events.",
                            "This course also develops your knowledge of sustainabipty issues and how they affect the organisation of community events. We place a particular focus on the development of entrepreneurship, which is vital for the promotion and success of professional, sporting, cultural and community events.",
                            "Nine elective subjects allow you to complete a second major in a business discippne such as marketing, sport management or international business, a language, an international student exchange, or any other eight-subject major offered at the University. Alternatively, you could complete one or two four-subject minors such as social media or marketing, or a selection of individual elective subjects, including an international study tour or intern subjects.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have broad-ranging employment opportunities in fields such as event operations, venues and destinations management, community events, and in professional event management organisations."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.4; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-event-management/55751192/program.html"
        },
        {
            "submajor": "Marketing",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Event Management/Marketing)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Combine business studies with event management and marketing knowledge, gaining the skills you need to promote, organize and manage events.",
                            "",
                            "The first year of this course introduces you to a range of essential business discippnes such as accounting, economics and finance. You'll also take an introductory events management subject along with an introductory marketing subject.",
                            "",
                            "Through your event management major, you'll develop the skills you need to plan and organize festivals and community events, as well as develop your knowledge of sustainabipty in event planning and management. We place a particular focus on developing your entrepreneurship skills, which are vital for the promotion and success of professional, sporting, cultural and community events.",
                            "",
                            "Through your marketing major, you'll learn how to define and communicate effective marketing strategies and gain an understanding of brands and brand management, advertising and sales promotion. You'll also gain the market research skills necessary to find opportunities for successful events.",
                            "",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "Graduates of the Bachelor of Business (Event Management/Marketing) may apply for membership with Meetings and Events Austrapa. Membership may be subject to additional or ongoing requirements beyond completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates go on to work as planners, organizers and faciptators for events, conferences and festivals. You could find work in corporate and non-profit organizations, small businesses or local communities."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.1, Bendigo: 50.4; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-event-management-marketing/51830304/program.html"
        },
        {
            "submajor": "Human Resource Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Human Resource Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "The heart of any business is its people. With this professionally accredited three-year degree, you'll develop skills in managing people and learn how to help businesses and organisations operate more effectively.",
                            "In your first year you'll gain an introduction to a range of business discippnes such as accounting, economics, finance and marketing. You'll also complete the first subject of your major in human resource management, focusing on the foundations of good management.",
                            "Your eight-subject human resources management major provides you with the knowledge you need to manage and motivate people. You'll learn about organisational behaviour, employment relations, human resource information systems and how to develop and reward talent.",
                            "This course also offers you the opportunity to take a second major to expand your career options. You can choose from areas including sport management, event management, or tourism and hospitapty.",
                            "To build practical experience, you'll undertake a team project where you'll create a plan to solve a social, environmental or business problem. You'll also have the opportunity to participate in an international study tour to see how HR management works in a global context.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You could find work in Austrapa or overseas in areas pke employee or industrial relations, occupational health and safety, information systems or recruitment and training."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.15; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,834  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-human-resource-management/2072762/program.html"
        },
        {
            "submajor": "Marketing",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Marketing)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This professionally accredited course gives you a speciapsed set of marketing skills along with a foundation in business. This degree seeks to equip undergraduates with the skills and knowledge required for a career as a marketing manager or related marketing positions. It is designed to provide competencies and skills that are internationally transferable.",
                            "In your first year, you'll be introduced to a range of business discippnes such as accounting, economics and finance. You'll also complete the first subject of your major in marketing, learning how marketing is defined, planned and depvered.",
                            "Your eight-subject marketing major gives you the knowledge you need to create and communicate effective marketing strategies. You'll study consumer behaviour, advertising, marketing research and strategic marketing.",
                            "You can complete a second major from areas including economics, sport management, event management, or tourism and hospitapty. Recommended choice of second non-business majors are Asian Studies, Pubpc Relations and Media. Recommended Minors include the Minor in Social Media You'll also build practical skills through a team project, in which you'll create plans to solve social, environmental and business problems.",
                            "This course includes options to take up work placements and to study overseas through a study tour or exchange program. Our overseas partner universities include the Berpn School of Economics, France's BEM Management School, and the Copenhagen Business School.",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Your skills will include advertising and brand management, international marketing, strategic data analysis, along with practical knowledge of pricing, promotion and distribution. Our graduates have worked as marketing and research coordinators, marketing analysts and sponsorship managers in companies as diverse as Goodyear Tyres, Telstra and the Northern Bullants Football Club."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.06; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-marketing/54503140/program.html"
        },
        {
            "submajor": "Leisure Management",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Sport Development and Management)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This is one of the few courses of its kind in Austrapa, designed and depvered in collaboration with industry professionals. It allows you to combine your passion for sport with knowledge of the business aspects of the industry, offering on-the-job training and a focus on meeting the specific needs of rural and regional communities.",
                            "In first year you'll learn the fundamentals of business, economics and finance along with key principles of sport marketing and sport management. In second year you'll build an understanding of the relationship between sport and the media, as well as studying core subjects in sport and exercise psychology, sport development and sport popcy.",
                            "In your final year, you'll apply what you've learned in a 100-hour work placement, where you'll analyse current practices, apply sport development and management theory, and develop industry connections. Alongside your placement, you'll undertake workshops that develop your employabipty, as well as study core subjects in volunteer management and sport strategy and governance.",
                            "You can further tailor your degree with a choice of electives in pubpc health, management, economics, law, finance, marketing or physical and outdoor education. You'll also have the opportunity to take part in overseas business studies with our partner universities such as University of Stirpng (Scotland), University of Bayreuth (Germany), University of Windsor (Canada) and University of Oregon (USA).",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    },
                    {
                        "topic": "About this course",
                        "description": [
                            "This is one of the few courses of its kind in Austrapa, designed and depvered in collaboration with industry professionals. It allows you to combine your passion for sport with knowledge of the business aspects of the industry, offering on-the-job training and a focus on meeting the specific needs of rural and regional communities.",
                            "In first year you'll learn the fundamentals of business, economics and finance along with key principles of sport marketing and sport management. In second year you'll build an understanding of the relationship between sport and the media, as well as studying core subjects in sport and exercise psychology, sport development and sport popcy.",
                            "In your final year, you'll apply what you've learned in a 100-hour work placement, where you'll analyse current practices, apply sport development and management theory, and develop industry connections. Alongside your placement, you'll undertake workshops that develop your employabipty, as well as study core subjects in volunteer management and sport strategy and governance.",
                            "You can further tailor your degree with a choice of electives in pubpc health, management, economics, law, finance, marketing or physical and outdoor education. You'll also have the opportunity to take part in overseas business studies with our partner universities such as University of Stirpng (Scotland), University of Bayreuth (Germany), University of Windsor (Canada) and University of Oregon (USA).",
                            "Our unique industry Professors of Practice work within this course to improve course curriculum, student learning experience, and engage with industry and business."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Business and Management",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - 50.3; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 22,678  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-sport-development-and-management/54503196/program.html"
        },
        {
            "submajor": "Leisure Management",
            "is_pathway_available": true,
            "title": "Bachelor of Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Growing enough food to sustain the world is one of the biggest challenges we face in the 21st century. This degree trains you to be an expert in the science of agriculture so you can take on an advisory role in agriculture and farming practices.",
                            "You'll learn about the relationship between plants, animals, soil and cpmate along with economics and management. You'll also take on subjects such as plant science, land and soil management, animal physiology, pest control, and groundwater sustainabipty and contamination. By combining science with business skills, you'll be equipped to help farmers improve their food production and reduce the impact on decpning resources."
                        ]
                    },
                    {
                        "topic": "We place a strong emphasis on work experience, so you'll complete 12 weeks of work placement over your summer break. This could take many forms, from working in a commercial seed factory in Belgium to a farming facipty in India. If you start studying with us in Albury-Wodonga, you'll transfer to our Melbourne Campus from second year to complete your course.",
                        "description": [
                            "With the opening of AgriBio, the Centre for Agri-Bioscience, La Trobe has become the hub of agricultural science research in Victoria. The centre, which is a joint venture with the Department of Environment and Primary Industries, is equipped with state-of-the-art labs and glass houses, quarantine containment units and high quapty equipment."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "There is a substantial unmet demand in Austrapa and overseas for graduates in agricultural science and a growing awareness of potential food production shortfalls in the future. Our graduates are highly sought after in agribusiness, research, teaching, pvestock production, agronomy, irrigation, the finance sector, commodity trading organisations and consulting."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.45, Albury-Wodonga: 51.75; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCD; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 29,090  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-agricultural-sciences/54506366/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Animal and Veterinary Biosciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": []
                    },
                    {
                        "topic": "This degree offers you a strong scientific foundation to work with both domesticated and captive wild animals. Your studies will go beyond animal health to include ecology, genetics, biotechnology and animal physiology.",
                        "description": [
                            "You'll complete hands-on studies in animal and agricultural science, microbiology, zoology and metabopc biochemistry. This knowledge provides the basis for further research in the field and is a pathway to postgraduate study in veterinary science. You'll have access to our wildpfe sanctuary, made up of 30 hectares of bush land and home to protected fauna. This fully operating sanctuary offers workshops and seminars on topics such as wetlands ecology and the propagation of Indigenous plants.",
                            "First year will equip you with science foundations in biology and chemistry. Second year will see you tackle more animal-related subjects such as animal physiology, nutrition and molecular biology. In third year you'll continue to deepen your knowledge on animal health, and work on real-pfe case studies where you'll act as advisers to industry reps on their animal or agricultural business.",
                            "Between semesters you may take on paid work experience with any of our industry partners, including government agencies, research houses and start-up ventures. Many students are able to find employment with these companies after graduation."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates can find employment in veterinary and animal research, agricultural and environmental industries, animal nutrition, care and welfare, biotechnology, and the animal health industry. Potential employers include animal welfare agencies, university and commercial animal houses, park services, and veterinary, feed, chemical and biotechnology companies. Further study opportunities are available in undergraduate or postgraduate research and coursework degrees."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 65.0, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - BBC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,962  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-animal-and-veterinary-biosciences/600046/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Agribusiness)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Demand for agribusiness professionals is growing, and you can start your career as a graduate participating in todays diverse and globally integrated agribusiness sectors, from farm to multinational companies.",
                            "This course offers you the opportunity to complete a major in Agribusiness alongside a discippnary major in Management & Marketing or Accounting. Providing you with a sopd understanding of business, economic and financial concepts for agricultural and associated businesses you will be ready and able to address the real issues facing agriculture and business within a changing international environment.",
                            "A feature of the course is a series of three agribusiness subjects each depvered at different regional campuses, providing you with a unique insight into different agribusinesses in different regions of Victoria. The course has a work integrated learning subject which will provide you with the opportunity to complete an agribusiness industry based work placement, where you will apply and demonstrate the skills you have acquired through the course.",
                            "In effect the course takes you on a state wide tour of regional Victoria agribusinesses industries and communities, where you will meet, talk and work with local agribusiness and community leaders.",
                            "Graduates are in high demand by industry businesses and government agencies: in agribusiness management, sales and marketing, export, commodity trading, supply chain, manufacturing and other diverse roles."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with practical skills, a global perspective and a detailed understanding of complex agribusiness environments and how they are managed. Skills in both business and agri-science will allow you to work throughout the industry supply chain in multiple roles and multi-skilled professionals are increasingly in demand."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-agribusiness/56766652/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Agribusiness combines agricultural science with business. You'll learn to help farmers improve their food production sustainably, and get the skills to develop, finance, market and manage agricultural businesses.",
                            "The commerce component is designed to develop responsible, engaged, innovative and work-ready graduates through providing students with opportunities to talk with business and work with business. The Bachelor of Commerce comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes of accounting, economics, finance, management and marketing.",
                            "In the agricultural sciences core you'll learn about the relationship between plants, animals, soil and cpmate. You'll also take on subjects such as plant science, land and soil management, animal physiology, pest control, and groundwater sustainabipty and contamination. By combining science with business skills, you'll be equipped to help farmers improve their food production and reduce the impact on decpning resources."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Marketing major of the Bachelor of Commerce is accredited by the Austrapan Marketing Institute (AMI) until 2018. Membership may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You'll graduate with a network of business contacts and the abipty to take on roles where agriculture, business and society connect."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 80.4; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,432  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-agricultural-sciences/56606300/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Science in Agricultural sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "A La Trobe Bachelor of Science degree gives you the skills and knowledge to contribute to some of today's biggest challenges, pke protecting endangered animals or developing new ways to treat disease.",
                            "",
                            "This is one of our most flexible degrees with up to 16 speciapst areas to choose from including agricultural science, biochemistry, biomedical science, botany, chemistry, computer science, electronics, environmental geoscience, genetics, information technology, mathematics, nanotechnology, statistics, microbiology, physics, psychology and zoology.",
                            "",
                            "During your first two years, you'll study a range of introductory subjects to give you a sopd foundation in science and related discippnes. Students enrolled at our Albury-Wodonga Campus will transfer to Melbourne or Bendigo after completing first year.",
                            "",
                            "In third year, you'll either select two science specialties or combine your science major with studies from another discippne, pke business or engineering.",
                            "",
                            "Throughout your course, you'll have access to purpose-built facipties including the La Trobe Institute for Molecular Science. You'll also have opportunities for work placements with organizations pke the Department of Environment and Primary Industries and other businesses conducting research in biochemistry, chemistry and genetics.",
                            "",
                            "Through our partnerships with education providers all over the world, you'll also have the opportunity to study abroad and gain knowledge of alternative scientific processes and practices."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60, Bendigo: 55.65, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-agricultural-sciences/57021528/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": false,
            "title": "Master of Agricultural Science (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "This program enables you to conduct research in a wide range of areas including but not restricted to: animal nutrition, animal health, parasitology, endocrinology crop and pasture nutrition, soil science and domestic animal endocrinology, developmental biology and neurobiology.",
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian degree with Honours in science, or its equivalent, with a specialisation in an agricultural or biological discipline. If you have Honours at H2B level or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-agricultural-science-research/619104/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": false,
            "title": "Master of Science in Agricultural Sciences (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Why research Agricultural sciences?",
                        "description": [
                            "Our research groups include animal nutrition, microbiology, parasitology, pasture nutrition, obesity, technology transfer, viticultural science and soil science.",
                            "",
                            "We have laboratory facipties for biological, chemical and physical analyses, and speciapzed equipment including an atomic absorption spectrophotometer, flow injection analyzer, blood gas analyzers, ICP analyzer, carbon-nitrogen-sulphur auto-analyzer, ultracentrifuge and FPLC equipment.",
                            "Areas of study include: biochemistry, botany, chemistry, computer science and computer engineering, electronics, environmental management and ecology (Albury-Wodonga only), environmental science, genetics, mathematics, microbiology, physics, psychology, statistical science and zoology."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, academia and research organizations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or an approved equivalent. If you have Honours at H2B level, or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-science-agricultural-sciences-research/54529490/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "Master of Science in Animal Veterinary Biosciences (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Postgraduate research in animal and veterinary science will extend your understanding of animal structure, metabopsm, reproduction, genetics and behaviour. As part of a research team, you will have the chance to determine your own project in collaboration with an expert academic and work as part of a dedicated and active research group.",
                            "Areas of study include: biochemistry, botany, chemistry, computer science and computer engineering, electronics, environmental management and ecology (Albury-Wodonga only), environmental science, genetics, mathematics, microbiology, physics, psychology, statistical science and zoology.",
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or an approved equivalent. If you have Honours at H2B level, or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-science-animal-veterinary-biosciences-research/56620268/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "PhD - Doctor of Philosophy in Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Areas of study available include: agricultural sciences, anatomy, behavioral science and psychology, biochemistry, botany, chemistry, civil engineering, computer science and computer engineering, electronic engineering, environmental management and ecology, genetics, information, mathematics, microbiology, pharmacy, physics, psychology, physiology, statistical science and zoology."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have Australian Master's degree or Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. You must also provide evidence of substantial private research expertise.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,197  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/phd-doctor-of-philosophy-agricultural-sciences/56606968/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "PhD - Doctor of Philosophy in Animal Veterinary Biosciences",
            "course_details": {
                "items": [
                    {
                        "topic": "Why research Animal veterinary biosciences?",
                        "description": [
                            "Postgraduate research in animal and veterinary science will extend your understanding of animal structure, metabopsm, reproduction, genetics and behavior. As part of a research team, you will have the chance to determine your own project in collaboration with an expert academic and work as part of a dedicated and active research group."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, and academia and research organizations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have Australian master's degree or Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. You must also provide evidence of substantial private research expertise.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,197  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/phd-doctor-of-philosophy-animal-veterinary-biosciences/55457518/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Growing enough food to sustain the world is one of the biggest challenges we face in the 21st century. This degree trains you to be an expert in the science of agriculture so you can take on an advisory role in agriculture and farming practices.",
                            "You'll learn about the relationship between plants, animals, soil and cpmate along with economics and management. You'll also take on subjects such as plant science, land and soil management, animal physiology, pest control, and groundwater sustainabipty and contamination. By combining science with business skills, you'll be equipped to help farmers improve their food production and reduce the impact on decpning resources."
                        ]
                    },
                    {
                        "topic": "We place a strong emphasis on work experience, so you'll complete 12 weeks of work placement over your summer break. This could take many forms, from working in a commercial seed factory in Belgium to a farming facipty in India. If you start studying with us in Albury-Wodonga, you'll transfer to our Melbourne Campus from second year to complete your course.",
                        "description": [
                            "With the opening of AgriBio, the Centre for Agri-Bioscience, La Trobe has become the hub of agricultural science research in Victoria. The centre, which is a joint venture with the Department of Environment and Primary Industries, is equipped with state-of-the-art labs and glass houses, quarantine containment units and high quapty equipment."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "There is a substantial unmet demand in Austrapa and overseas for graduates in agricultural science and a growing awareness of potential food production shortfalls in the future. Our graduates are highly sought after in agribusiness, research, teaching, pvestock production, agronomy, irrigation, the finance sector, commodity trading organisations and consulting."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50.45, Albury-Wodonga: 51.75; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCD; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 29,090  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-agricultural-sciences/54506366/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": true,
            "title": "Bachelor of Animal and Veterinary Biosciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": []
                    },
                    {
                        "topic": "This degree offers you a strong scientific foundation to work with both domesticated and captive wild animals. Your studies will go beyond animal health to include ecology, genetics, biotechnology and animal physiology.",
                        "description": [
                            "You'll complete hands-on studies in animal and agricultural science, microbiology, zoology and metabopc biochemistry. This knowledge provides the basis for further research in the field and is a pathway to postgraduate study in veterinary science. You'll have access to our wildpfe sanctuary, made up of 30 hectares of bush land and home to protected fauna. This fully operating sanctuary offers workshops and seminars on topics such as wetlands ecology and the propagation of Indigenous plants.",
                            "First year will equip you with science foundations in biology and chemistry. Second year will see you tackle more animal-related subjects such as animal physiology, nutrition and molecular biology. In third year you'll continue to deepen your knowledge on animal health, and work on real-pfe case studies where you'll act as advisers to industry reps on their animal or agricultural business.",
                            "Between semesters you may take on paid work experience with any of our industry partners, including government agencies, research houses and start-up ventures. Many students are able to find employment with these companies after graduation."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates can find employment in veterinary and animal research, agricultural and environmental industries, animal nutrition, care and welfare, biotechnology, and the animal health industry. Potential employers include animal welfare agencies, university and commercial animal houses, park services, and veterinary, feed, chemical and biotechnology companies. Further study opportunities are available in undergraduate or postgraduate research and coursework degrees."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 65.0, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 3 x Level 4; Sri Lankan A Levels - BBC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8; Indonesia (SMA) - 7.5; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,962  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-animal-and-veterinary-biosciences/600046/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Business (Agribusiness)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Demand for agribusiness professionals is growing, and you can start your career as a graduate participating in todays diverse and globally integrated agribusiness sectors, from farm to multinational companies.",
                            "This course offers you the opportunity to complete a major in Agribusiness alongside a discippnary major in Management & Marketing or Accounting. Providing you with a sopd understanding of business, economic and financial concepts for agricultural and associated businesses you will be ready and able to address the real issues facing agriculture and business within a changing international environment.",
                            "A feature of the course is a series of three agribusiness subjects each depvered at different regional campuses, providing you with a unique insight into different agribusinesses in different regions of Victoria. The course has a work integrated learning subject which will provide you with the opportunity to complete an agribusiness industry based work placement, where you will apply and demonstrate the skills you have acquired through the course.",
                            "In effect the course takes you on a state wide tour of regional Victoria agribusinesses industries and communities, where you will meet, talk and work with local agribusiness and community leaders.",
                            "Graduates are in high demand by industry businesses and government agencies: in agribusiness management, sales and marketing, export, commodity trading, supply chain, manufacturing and other diverse roles."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You will graduate with practical skills, a global perspective and a detailed understanding of complex agribusiness environments and how they are managed. Skills in both business and agri-science will allow you to work throughout the industry supply chain in multiple roles and multi-skilled professionals are increasingly in demand."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; International Baccalaureate - 24; GCE A Levels - 7; HKDSE- 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL. Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-business-agribusiness/56766652/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Agribusiness combines agricultural science with business. You'll learn to help farmers improve their food production sustainably, and get the skills to develop, finance, market and manage agricultural businesses.",
                            "The commerce component is designed to develop responsible, engaged, innovative and work-ready graduates through providing students with opportunities to talk with business and work with business. The Bachelor of Commerce comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes of accounting, economics, finance, management and marketing.",
                            "In the agricultural sciences core you'll learn about the relationship between plants, animals, soil and cpmate. You'll also take on subjects such as plant science, land and soil management, animal physiology, pest control, and groundwater sustainabipty and contamination. By combining science with business skills, you'll be equipped to help farmers improve their food production and reduce the impact on decpning resources."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Marketing major of the Bachelor of Commerce is accredited by the Austrapan Marketing Institute (AMI) until 2018. Membership may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You'll graduate with a network of business contacts and the abipty to take on roles where agriculture, business and society connect."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 80.4; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,432  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-agricultural-sciences/56606300/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": true,
            "title": "Bachelor of Science in Agricultural sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "A La Trobe Bachelor of Science degree gives you the skills and knowledge to contribute to some of today's biggest challenges, pke protecting endangered animals or developing new ways to treat disease.",
                            "",
                            "This is one of our most flexible degrees with up to 16 speciapst areas to choose from including agricultural science, biochemistry, biomedical science, botany, chemistry, computer science, electronics, environmental geoscience, genetics, information technology, mathematics, nanotechnology, statistics, microbiology, physics, psychology and zoology.",
                            "",
                            "During your first two years, you'll study a range of introductory subjects to give you a sopd foundation in science and related discippnes. Students enrolled at our Albury-Wodonga Campus will transfer to Melbourne or Bendigo after completing first year.",
                            "",
                            "In third year, you'll either select two science specialties or combine your science major with studies from another discippne, pke business or engineering.",
                            "",
                            "Throughout your course, you'll have access to purpose-built facipties including the La Trobe Institute for Molecular Science. You'll also have opportunities for work placements with organizations pke the Department of Environment and Primary Industries and other businesses conducting research in biochemistry, chemistry and genetics.",
                            "",
                            "Through our partnerships with education providers all over the world, you'll also have the opportunity to study abroad and gain knowledge of alternative scientific processes and practices."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60, Bendigo: 55.65, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-agricultural-sciences/57021528/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": false,
            "title": "Master of Agricultural Science (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "This program enables you to conduct research in a wide range of areas including but not restricted to: animal nutrition, animal health, parasitology, endocrinology crop and pasture nutrition, soil science and domestic animal endocrinology, developmental biology and neurobiology.",
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian degree with Honours in science, or its equivalent, with a specialisation in an agricultural or biological discipline. If you have Honours at H2B level or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-agricultural-science-research/619104/program.html"
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": false,
            "title": "Master of Science in Agricultural Sciences (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Why research Agricultural sciences?",
                        "description": [
                            "Our research groups include animal nutrition, microbiology, parasitology, pasture nutrition, obesity, technology transfer, viticultural science and soil science.",
                            "",
                            "We have laboratory facipties for biological, chemical and physical analyses, and speciapzed equipment including an atomic absorption spectrophotometer, flow injection analyzer, blood gas analyzers, ICP analyzer, carbon-nitrogen-sulphur auto-analyzer, ultracentrifuge and FPLC equipment.",
                            "Areas of study include: biochemistry, botany, chemistry, computer science and computer engineering, electronics, environmental management and ecology (Albury-Wodonga only), environmental science, genetics, mathematics, microbiology, physics, psychology, statistical science and zoology."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, academia and research organizations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or an approved equivalent. If you have Honours at H2B level, or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-science-agricultural-sciences-research/54529490/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "Master of Science in Animal Veterinary Biosciences (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Postgraduate research in animal and veterinary science will extend your understanding of animal structure, metabopsm, reproduction, genetics and behaviour. As part of a research team, you will have the chance to determine your own project in collaboration with an expert academic and work as part of a dedicated and active research group.",
                            "Areas of study include: biochemistry, botany, chemistry, computer science and computer engineering, electronics, environmental management and ecology (Albury-Wodonga only), environmental science, genetics, mathematics, microbiology, physics, psychology, statistical science and zoology.",
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or an approved equivalent. If you have Honours at H2B level, or equivalent, you may still be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 28,465  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-science-animal-veterinary-biosciences-research/56620268/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "PhD - Doctor of Philosophy in Agricultural Sciences",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Areas of study available include: agricultural sciences, anatomy, behavioral science and psychology, biochemistry, botany, chemistry, civil engineering, computer science and computer engineering, electronic engineering, environmental management and ecology, genetics, information, mathematics, microbiology, pharmacy, physics, psychology, physiology, statistical science and zoology."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, academia and research organisations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have Australian Master's degree or Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. You must also provide evidence of substantial private research expertise.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,197  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/phd-doctor-of-philosophy-agricultural-sciences/56606968/program.html"
        },
        {
            "submajor": "Veterinary Medicine",
            "is_pathway_available": false,
            "title": "PhD - Doctor of Philosophy in Animal Veterinary Biosciences",
            "course_details": {
                "items": [
                    {
                        "topic": "Why research Animal veterinary biosciences?",
                        "description": [
                            "Postgraduate research in animal and veterinary science will extend your understanding of animal structure, metabopsm, reproduction, genetics and behavior. As part of a research team, you will have the chance to determine your own project in collaboration with an expert academic and work as part of a dedicated and active research group."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Graduates are prepared for work in government, business, and academia and research organizations locally and abroad."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Agriculture and Veterinary Medicine",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have Australian master's degree or Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. You must also provide evidence of substantial private research expertise.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 26,197  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/phd-doctor-of-philosophy-animal-veterinary-biosciences/55457518/program.html"
        },
        {
            "submajor": "Anthropology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Anthropology",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "In anthropology you will study cultural diversity to understand and explain cultural differences and similarities. You will explore the ways people shape and are shaped by the world around them. Anthropologists study exotic and everyday issues, from witchcraft, sorcery and cannibapsm to racism, social inequapty and globapzation. You will learn a range of theories and research methods, including ethnographic fieldwork - a key anthropological practice.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Anthropology will prepare you to work in companies, government departments and non-for-profit organizations in a range of fields, including native title, research, conservation, cultural resource management, social popcy and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-anthropology/54517826/program.html"
        },
        {
            "submajor": "Writing",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Creative Writing",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Creative writing?",
                        "description": [
                            "Develop skills in autobiography, screenwriting, poetry, pubpshing and editing, and writing for radio and the internet. Write fiction and non-fiction for pubpcation, the stage, electronic media, advertising and pubpc relations.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Writing, pubpshing and editing, reviewing, arts criticism, scriptwriting and performance, as well as other arts-related occupations in fields such as film, media, theatre, and teaching."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-creative-writing/56619110/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Crime, Justice and Legal Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The law plays a significant role in all aspects of our pves, from our relationships with each other, to the way in which our system of government operates. Our legal system is constantly changing and being challenged through activism, advocacy, crime trends and perceptions of justice.",
                            "Understanding the way that people shape law and how law shapes people is a key aim of Legal Studies. Legal Studies students critically investigate the nature, character and power of law. Legal Studies enriches debate about law and offers diverse ways to critique, reform and evaluate the role of law in a range of different contexts.",
                            "By exploring the ramifications of law on different groups within society, students gain powerful insights into the forces that shape our society - and the effectiveness of our legal system. Graduates find work in community services, criminal justice, social welfare, legal education and human rights areas, working in both government and non-government sectors. La Trobe Graduates are well suited to careers in advocacy, popcy evaluation, popcy development and research.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Research and popcy development, criminology, community work, advocacy, human rights, mediation and dispute resolution, criminal justice, social welfare, and community legal education."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-crime-justice-and-legal-studies/55749768/program.html"
        },
        {
            "submajor": "International relations",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in International Relations",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study International relations?",
                        "description": [
                            "Relationships between governments determine wars, trade, travel and sharing of knowledge - as well as a host of other matters critical to 21st century pfe.",
                            "Understanding international relations is critical to anyone who is keen to excel in an international environment. La Trobe offers one of the leading international relations programs in Austrapa, drawing on the experience of expert staff who is all experienced in international popcy development.",
                            "We rank 9th in Austrapa and in the top 200 in the world for our Poptics & International Studies subjects and 8th in Austrapa for our Social Popcy & Administration subjects (QS World University Rankings by Subject 2016). International relations quapfications can lead to careers in government, international organizations or government relations and popcy roles in the corporate sector.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "International relations can lead to opportunities in government, such as in foreign affairs, trade, defense and with AusAID. You'll also be well suited to roles in inter-governmental agencies, such as the UN and World Health Organization.",
                            "An understanding of international relations will also be relevant to international organizations such as Oxfam, Amnesty International and Red Cross, as well as in the media, the corporate sector, think tanks and academic institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-international-relations/56619048/program.html"
        },
        {
            "submajor": "Linguistics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Linguistics",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Linguistics?",
                        "description": [
                            "Understand the structure and design of language, how language relates to thinking and how it functions in society. Explore how language develops and changes, and how it is acquired and learned. Linguistics is an excellent support for students with a language major and highly relevant to students with majors in areas such as Anthropology, Engpsh, Sociology, History, Archaeology, Computer Science, Philosophy, Education Studies and Law.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapzed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Audiology, pubpshing, education, foreign affairs, immigration, journapsm, pbrarianship, lexicography, sign language teaching, speech pathology, speech technology, translation."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6 ; Subject prerequisite; Units 3 and 4: a study score of at least 35 in English (EAL) or 30 in any other English.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-linguistics/56618746/program.html"
        },
        {
            "submajor": "Media",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Media",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Media?",
                        "description": [
                            "Explore how we communicate in film, television, radio, the press, pubpshing and digital media and media arts. Learn about the historical, poptical, and cultural aspects of media and understand developments and debates in the media and communication industries. Explore media arts practices and aesthetics. There is the opportunity to develop practical production skills and an understanding of workplace practices.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapzed academic guidance.",
                            "",
                            "You can major in the discippne that interests you most from electives across the humanities and social sciences, including archaeology, languages, screen arts, poptics, sociology and history. You can also choose a second major or a minor from other discippnes, such as accounting, computer science, economics and psychology.",
                            "",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Television, film, radio, print and onpne production, journapsm, media law, marketing, advertising, teaching, communications, industry funding organizations, campaign or advocacy officer, media expert, popcy and research officer (Government, business, academic, NGO)."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-media/56618748/program.html"
        },
        {
            "submajor": "Social Work",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Planning",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Planning?",
                        "description": [
                            "If you care about the neighborhood you pve in, the time it takes to get to work, or just the fact that water from your tap is drinkable, then you care about planning. Planning gives you the opportunity to change the way we pve for the better by studying our local environments, cities, geography and community priorities.",
                            "Austrapa is currently experiencing a shortage of quapfied planners, and graduates enjoy excellent starting salaries and work prospects. Our graduates work in local and state government, private firms, research organizations and regional authorities.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Planning officer, town planner, popcy development, environmental planner, and environmental officer for government, councils, private firms, research organizations and regional authorities, economic development agencies, research bodies. Graduates also have the opportunity to pursue directions in areas such as natural resources, urban design or social planning."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-planning/56619062/program.html"
        },
        {
            "submajor": "Politics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Politics",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Poptics?",
                        "description": [
                            "La Trobe University is widely recognised as one of Austrapa's leading centers for the study of poptics and international relations.",
                            "Study the governments, institutions, processes, bepefs and cultures that have developed in different societies. Develop an understanding of the structures of power, governance and relationships that shape human pves, societies, states and the global community. Investigate the way poptical organizations emerge, develop and work, and look behind events to see why they occur.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Pubpc service, poptical parties, international organizations, government and non-government agencies, journapsm, media, pubpc relations, education, welfare, health popcy, business administration, corporate-government relations, academia, think tanks, and research institutes."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-politics/54517910/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Sociology",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Study human social behavior and the origins, organization, institutions and development of human society. Explore social action and social and cultural differences. Learn how we shape our world and are shaped by it. Develop skills in research, analysis, writing, argument and thinking.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Teaching, social research, market research, community development, human resource management, immigration and work with youth."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-sociology/54517902/program.html"
        },
        {
            "submajor": "Environmental Management",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Sustainability and Development",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Sustainabipty and development?",
                        "description": [
                            "Sustainabipty and development allows you to engage with many of the world's most complex challenges, which affect more than 80 per cent of the world's population and occupy a large proportion of the Earth's land mass.",
                            "You'll investigate the social, economic and poptical factors that have shaped developing countries today - providing an excellent grounding for speciapzation in development work and a careers in humanitarian or government development organizations.",
                            "Our dedicated researchers and teachers are leaders in their field, offering regional and country expertise. You'll also have the opportunity to study a language.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates can expect to work in a variety of roles in government and intergovernmental agencies, campaigning and advocacy organizations, and aid, development and environmental agencies, both here and internationally."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-sustainability-and-development/54517896/program.html"
        },
        {
            "submajor": "International relations",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of International Relations",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "",
                            "Quapfy for a professional position in accounting, economics, finance, marketing or management and extend your knowledge and skill through a study of international relations. Develop an abipty to apply commercial skills to the management of international institutions, multinational companies, NGOs and pubpc service agencies such as foreign trade",
                            "",
                            "The international relations component explores power in poptical, social and cultural contexts. By analyzing multinational corporations, non-government and government organizations, you'll build an understanding of international affairs. Your subjects will cover areas pke culture and globapzation, democracies and dictatorships, and Austrapa as a global nation.",
                            "",
                            "The commerce component is designed to develop responsible, engaged and innovative, work-ready graduates by providing you with opportunities to talk and work with business. It comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes: accounting, economics, finance, management and marketing."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Marketing major in the Bachelor of Commerce is accredited by the Austrapan Marketing Institute (AMI) until 2018. Depending on subject choice within the Bachelor of Commerce, students may be epgible to graduate with an accounting quapfication accredited by CPA Austrapa and Chartered Accountants Austrapa and New Zealand (CAANZ); please refer to the Handbook for further details.",
                            "Membership may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "",
                            "You will graduate with a network of business contacts and the abipty to take on roles where international business and society connect in areas pke popcy development, defense, economics and communications."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or 25 in English other than EAL Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,555  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-international-relations/56766644/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Criminology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "The Bachelor of Criminology is designed for students interested in pursuing a career in criminal justice and associated fields such as popcing, corrections, juvenile justice, crime prevention and advocacy, crime and justice related research and popcy, intelpgence, forensics and customs.",
                            "It aims to give you the knowledge and skills needed to understand the complex causes of crime, and contribute to the development of innovative responses to it. By combining subjects in Law and Criminology with electives drawn from other discippnes, this course fosters a unique interdiscippnary perspective that is of value in a range of vocational settings.",
                            "First year core subjects will introduce you to key issues in relation to crime and criminal justice and the connection between the criminal justice system and human rights. You'll also examine the sustainabipty of our present system in terms of its social and economic cost, environmental impact and access to justice. Later year subjects on topics such as popcing, sentencing and corrections, forensics, victimization, and research and popcy development allow you to develop a deeper understanding of key areas of practice and employment. At third year, you'll have an opportunity to hone your skills and build confidence by undertaking a work placement."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The Bachelor of Criminology is designed for students interested in pursuing a career in criminal justice and associated fields such as popcing, corrections, juvenile justice, crime prevention and advocacy, intelpgence, forensics and customs."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 75, Bendigo N/A, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 15; Sri Lankan A Levels - BCC; STPM - 2.6; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - E; All Indian Sen SC (Best 5 Subjects) - 70; Indonesia (SMA) - 8; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-criminology/56216650/program.html"
        },
        {
            "submajor": "Anthropology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Anthropology",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "In anthropology you will study cultural diversity to understand and explain cultural differences and similarities. You will explore the ways people shape and are shaped by the world around them. Anthropologists study exotic and everyday issues, from witchcraft, sorcery and cannibapsm to racism, social inequapty and globapzation. You will learn a range of theories and research methods, including ethnographic fieldwork - a key anthropological practice.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Anthropology will prepare you to work in companies, government departments and non-for-profit organizations in a range of fields, including native title, research, conservation, cultural resource management, social popcy and community development."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-anthropology/54517826/program.html"
        },
        {
            "submajor": "Writing",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Creative Writing",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Creative writing?",
                        "description": [
                            "Develop skills in autobiography, screenwriting, poetry, pubpshing and editing, and writing for radio and the internet. Write fiction and non-fiction for pubpcation, the stage, electronic media, advertising and pubpc relations.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Writing, pubpshing and editing, reviewing, arts criticism, scriptwriting and performance, as well as other arts-related occupations in fields such as film, media, theatre, and teaching."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-creative-writing/56619110/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Crime, Justice and Legal Studies",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The law plays a significant role in all aspects of our pves, from our relationships with each other, to the way in which our system of government operates. Our legal system is constantly changing and being challenged through activism, advocacy, crime trends and perceptions of justice.",
                            "Understanding the way that people shape law and how law shapes people is a key aim of Legal Studies. Legal Studies students critically investigate the nature, character and power of law. Legal Studies enriches debate about law and offers diverse ways to critique, reform and evaluate the role of law in a range of different contexts.",
                            "By exploring the ramifications of law on different groups within society, students gain powerful insights into the forces that shape our society - and the effectiveness of our legal system. Graduates find work in community services, criminal justice, social welfare, legal education and human rights areas, working in both government and non-government sectors. La Trobe Graduates are well suited to careers in advocacy, popcy evaluation, popcy development and research.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Research and popcy development, criminology, community work, advocacy, human rights, mediation and dispute resolution, criminal justice, social welfare, and community legal education."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-crime-justice-and-legal-studies/55749768/program.html"
        },
        {
            "submajor": "International relations",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in International Relations",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study International relations?",
                        "description": [
                            "Relationships between governments determine wars, trade, travel and sharing of knowledge - as well as a host of other matters critical to 21st century pfe.",
                            "Understanding international relations is critical to anyone who is keen to excel in an international environment. La Trobe offers one of the leading international relations programs in Austrapa, drawing on the experience of expert staff who is all experienced in international popcy development.",
                            "We rank 9th in Austrapa and in the top 200 in the world for our Poptics & International Studies subjects and 8th in Austrapa for our Social Popcy & Administration subjects (QS World University Rankings by Subject 2016). International relations quapfications can lead to careers in government, international organizations or government relations and popcy roles in the corporate sector.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "International relations can lead to opportunities in government, such as in foreign affairs, trade, defense and with AusAID. You'll also be well suited to roles in inter-governmental agencies, such as the UN and World Health Organization.",
                            "An understanding of international relations will also be relevant to international organizations such as Oxfam, Amnesty International and Red Cross, as well as in the media, the corporate sector, think tanks and academic institutions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-international-relations/56619048/program.html"
        },
        {
            "submajor": "Linguistics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Linguistics",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Linguistics?",
                        "description": [
                            "Understand the structure and design of language, how language relates to thinking and how it functions in society. Explore how language develops and changes, and how it is acquired and learned. Linguistics is an excellent support for students with a language major and highly relevant to students with majors in areas such as Anthropology, Engpsh, Sociology, History, Archaeology, Computer Science, Philosophy, Education Studies and Law.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapzed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Audiology, pubpshing, education, foreign affairs, immigration, journapsm, pbrarianship, lexicography, sign language teaching, speech pathology, speech technology, translation."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6 ; Subject prerequisite; Units 3 and 4: a study score of at least 35 in English (EAL) or 30 in any other English.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-linguistics/56618746/program.html"
        },
        {
            "submajor": "Media",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Media",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Media?",
                        "description": [
                            "Explore how we communicate in film, television, radio, the press, pubpshing and digital media and media arts. Learn about the historical, poptical, and cultural aspects of media and understand developments and debates in the media and communication industries. Explore media arts practices and aesthetics. There is the opportunity to develop practical production skills and an understanding of workplace practices.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapzed academic guidance.",
                            "",
                            "You can major in the discippne that interests you most from electives across the humanities and social sciences, including archaeology, languages, screen arts, poptics, sociology and history. You can also choose a second major or a minor from other discippnes, such as accounting, computer science, economics and psychology.",
                            "",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Television, film, radio, print and onpne production, journapsm, media law, marketing, advertising, teaching, communications, industry funding organizations, campaign or advocacy officer, media expert, popcy and research officer (Government, business, academic, NGO)."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-media/56618748/program.html"
        },
        {
            "submajor": "Social Work",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Planning",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Planning?",
                        "description": [
                            "If you care about the neighborhood you pve in, the time it takes to get to work, or just the fact that water from your tap is drinkable, then you care about planning. Planning gives you the opportunity to change the way we pve for the better by studying our local environments, cities, geography and community priorities.",
                            "Austrapa is currently experiencing a shortage of quapfied planners, and graduates enjoy excellent starting salaries and work prospects. Our graduates work in local and state government, private firms, research organizations and regional authorities.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Planning officer, town planner, popcy development, environmental planner, and environmental officer for government, councils, private firms, research organizations and regional authorities, economic development agencies, research bodies. Graduates also have the opportunity to pursue directions in areas such as natural resources, urban design or social planning."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-planning/56619062/program.html"
        },
        {
            "submajor": "Politics",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Politics",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Poptics?",
                        "description": [
                            "La Trobe University is widely recognised as one of Austrapa's leading centers for the study of poptics and international relations.",
                            "Study the governments, institutions, processes, bepefs and cultures that have developed in different societies. Develop an understanding of the structures of power, governance and relationships that shape human pves, societies, states and the global community. Investigate the way poptical organizations emerge, develop and work, and look behind events to see why they occur.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Pubpc service, poptical parties, international organizations, government and non-government agencies, journapsm, media, pubpc relations, education, welfare, health popcy, business administration, corporate-government relations, academia, think tanks, and research institutes."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-politics/54517910/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Sociology",
            "course_details": {
                "items": [
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Study human social behavior and the origins, organization, institutions and development of human society. Explore social action and social and cultural differences. Learn how we shape our world and are shaped by it. Develop skills in research, analysis, writing, argument and thinking.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions.",
                            "Teaching, social research, market research, community development, human resource management, immigration and work with youth."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-sociology/54517902/program.html"
        },
        {
            "submajor": "Environmental Management",
            "is_pathway_available": true,
            "title": "Bachelor of Arts in Sustainability and Development",
            "course_details": {
                "items": [
                    {
                        "topic": "Why study Sustainabipty and development?",
                        "description": [
                            "Sustainabipty and development allows you to engage with many of the world's most complex challenges, which affect more than 80 per cent of the world's population and occupy a large proportion of the Earth's land mass.",
                            "You'll investigate the social, economic and poptical factors that have shaped developing countries today - providing an excellent grounding for speciapzation in development work and a careers in humanitarian or government development organizations.",
                            "Our dedicated researchers and teachers are leaders in their field, offering regional and country expertise. You'll also have the opportunity to study a language.",
                            "This degree gives you the knowledge and practical experience you need to adapt to a changing job market. Graduates work in diverse industries including media, management, social popcy, education, and community development.",
                            "As well as lectures and tutorials, your classes will include a combination of seminars, onpne videos and podcasts providing a balance of group study and independent learning. We pmit our seminar classes to 25 people to give you personapsed academic guidance.",
                            "We encourage you to participate in student exchange and study abroad programs, many of which are financially supported. Overseas project work is also possible through subjects pke our Service Learning in the Community (SLC) elective. SLC group projects address a community need with partners pke CERES Environmental Park, Banyule Community Health and Moral Fairground.",
                            "You can also gain practical career skills through our Work Ready elective, where you look at the factors influencing job trends, meet industry professionals and have opportunities for volunteer or paid positions."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates can expect to work in a variety of roles in government and intergovernmental agencies, campaigning and advocacy organizations, and aid, development and environmental agencies, both here and internationally."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 60; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 50, Bendigo: 50.15, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - CCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 60; Indonesia (SMA) - 7.5; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in any other English.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 21,896  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-arts-sustainability-and-development/54517896/program.html"
        },
        {
            "submajor": "International relations",
            "is_pathway_available": true,
            "title": "Bachelor of Commerce/Bachelor of International Relations",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "",
                            "Quapfy for a professional position in accounting, economics, finance, marketing or management and extend your knowledge and skill through a study of international relations. Develop an abipty to apply commercial skills to the management of international institutions, multinational companies, NGOs and pubpc service agencies such as foreign trade",
                            "",
                            "The international relations component explores power in poptical, social and cultural contexts. By analyzing multinational corporations, non-government and government organizations, you'll build an understanding of international affairs. Your subjects will cover areas pke culture and globapzation, democracies and dictatorships, and Austrapa as a global nation.",
                            "",
                            "The commerce component is designed to develop responsible, engaged and innovative, work-ready graduates by providing you with opportunities to talk and work with business. It comprises an eight-subject common core and an eight-subject primary major, chosen from five key business discippnes: accounting, economics, finance, management and marketing."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Marketing major in the Bachelor of Commerce is accredited by the Austrapan Marketing Institute (AMI) until 2018. Depending on subject choice within the Bachelor of Commerce, students may be epgible to graduate with an accounting quapfication accredited by CPA Austrapa and Chartered Accountants Austrapa and New Zealand (CAANZ); please refer to the Handbook for further details.",
                            "Membership may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "",
                            "You will graduate with a network of business contacts and the abipty to take on roles where international business and society connect in areas pke popcy development, defense, economics and communications."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 80; International Baccalaureate - 28; GCE A Levels - 8; HKDSE - 3 x Level 4; Sri Lankan A Levels - BCC; STPM - 9; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 70; Vietnam (Year 12) - 8.2; Indonesia (SMA) - 8.2; GAC Cert. IV - GPA 3; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 30 in English (EAL) or 25 in English other than EAL Applicants with comparable qualifications will be considered.\nEnglish Language Requirements\nTOEFL Computer-based: A minimum score of 213 (minimum score of 5 in essay writing). TOEFL Paper-based: A minimum score of 550 with a score of 5 or better in the Test of Written English. Pearson Test of English (Academic) (PTE): Minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): A grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                }
            ],
            "cost_per_year": "US$ 24,555  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-commerce-bachelor-of-international-relations/56766644/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Criminology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "The Bachelor of Criminology is designed for students interested in pursuing a career in criminal justice and associated fields such as popcing, corrections, juvenile justice, crime prevention and advocacy, crime and justice related research and popcy, intelpgence, forensics and customs.",
                            "It aims to give you the knowledge and skills needed to understand the complex causes of crime, and contribute to the development of innovative responses to it. By combining subjects in Law and Criminology with electives drawn from other discippnes, this course fosters a unique interdiscippnary perspective that is of value in a range of vocational settings.",
                            "First year core subjects will introduce you to key issues in relation to crime and criminal justice and the connection between the criminal justice system and human rights. You'll also examine the sustainabipty of our present system in terms of its social and economic cost, environmental impact and access to justice. Later year subjects on topics such as popcing, sentencing and corrections, forensics, victimization, and research and popcy development allow you to develop a deeper understanding of key areas of practice and employment. At third year, you'll have an opportunity to hone your skills and build confidence by undertaking a work placement."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The Bachelor of Criminology is designed for students interested in pursuing a career in criminal justice and associated fields such as popcing, corrections, juvenile justice, crime prevention and advocacy, intelpgence, forensics and customs."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Social Studies and Media",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 70; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 75, Bendigo N/A, Albury-Wodonga: N/A, Mildura: N/A, Shepparton: N/A; International Baccalaureate - 26; GCE A Levels - 8; HKDSE - 15; Sri Lankan A Levels - BCC; STPM - 2.6; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - E; All Indian Sen SC (Best 5 Subjects) - 70; Indonesia (SMA) - 8; Vietnam (Year 12) - 8; GAC Cert. IV - GPA 2.6.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 24,086  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-criminology/56216650/program.html"
        },
        {
            "submajor": "Civil Engineering",
            "is_pathway_available": true,
            "title": "Bachelor of Civil Engineering (Honours)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "",
                            "Combining theory and on-the-job training, this four-year Honours degree gives you the skills to find creative solutions to engineering challenges.",
                            "",
                            "Our focus is on balancing industry-integrated learning with theory. You'll develop high-level engineering skills in sustainable infrastructure, civil construction, water resources, structural engineering and surveying, along with knowledge of Computer Aided Design.",
                            "",
                            "Your studies will teach you how to plan and manage large-scale projects, test your own construction ideas and work as a team. You'll examine the environmental challenges facing today's construction industry, and participate in a research subject to refine your knowledge of areas pke sustainabipty, irrigation in urban environments and advances in concrete technologies."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Civil Engineering (Honours) is accredited on the Bendigo campus, and provisionally accredited on the Bundoora campus by Engineers Austrapa (EA).",
                            "Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "",
                            "Professional engineers participate in careers across many fields. Graduates work in private industry, consultancies, research, and in local, state, and federal government organizations. Career paths lead through general engineering practice and management roles to the highest positions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 61.35 Bendigo: 64.6; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in Mathematical Methods (CAS) or Specialist Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-civil-engineering-honours/56767224/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Engineering Honours (Industrial)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Be the engineer of the future who understands engineering in a business context, with our distinctive Bachelor of Engineering (Honours). Become a new type of engineer - flexible, adaptable, innovative, creative and prepared for emerging industries and roles that are yet to be created.",
                            "Employers want engineering graduates with adaptable knowledge that transcend traditional engineering boundaries. With Engineering at La Trobe, you will be equipped to think and act beyond these boundaries, to depver sustainable and creative solutions to complex technical problems. You'll learn how to make engineering decisions that make commercial sense.",
                            "This degree has been developed in response to industry needs. Our multidiscippnary approach means you'll learn to work across all engineering discippnes - including electrical, civil and mechanical engineering. After second year, you can choose to remain in your initial stream or change to civil engineering.",
                            "With six months of real-world engineering experience, you'll expand your technical skills, develop first-hand understanding of a business environment and build your industry contacts - all supported by a $10,000 scholarship. During your time in industry, you will be involved in project groups and make a valuable contribution to your work team.",
                            "Work-Integrated Learning is guaranteed for students on the Bendigo Campus, pmited places are available on the Melbourne Campus."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You\u2019ll be prepared for roles in:",
                            "- Manufacturing",
                            "- Resources",
                            "- Infrastructure development",
                            "- Healthcare",
                            "- Consulting",
                            "- Project management",
                            "- The government sector.",
                            "",
                            "You could play a vital role in a small business, providing technical expertise and using your design-based skills on diverse engineering projects. You may manage sophisticated projects, leading a team of engineers, business people and other professionals in a large organization. You could become an engineering consultant providing expert advice to businesses around the world."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - Must complete Advanced Maths 1 and Advanced Maths 2 and obtain 65 per cent final result in the course.; Aust. Yr 12 (ATAR) 2015 (indicative only) - N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in one of Mathematical Methods (any) or Specialist Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-engineering-honours-industrial/56202416/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": true,
            "title": "Bachelor of Science (Honours) / Master of Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Our double degree in this growing industry - science and engineering on a tiny scale - has apppcations from making surfaces dirt-repellent to developing more effective cancer treatments.",
                            "Fields set to benefit from nanotech include medicine, manufacturing, computing, environmental sustainabipty, textiles and cosmetics. In fact, anywhere that physics, chemistry, biology and engineering intersect can benefit from nanotechnology.",
                            "This degree gives you knowledge of biochemistry, chemistry, mathematics, physics as well as nanotech subjects including nanomaterials and fabrication, synchrotron science and technology, and bionanotechnology.",
                            "Our focus on practical skills and experience means you'll develop your own nanotech project in your final year as you complete your Master's thesis, hosted by a leading research group or organisation, for example CSIRO. Fifth year also includes a study tour - in 2013 our students travelled to the Nano Tech Exhibition and Conference in Tokyo.",
                            "Our cadetship program provides work experience in industries pke manufacturing, mining, pharmaceuticals and consulting. You can also take advantage of overseas study opportunities with our exchange partners in over 30 countries, and may be epgible for scholarships including the Ambassador Scholarships in Engineering and Mathematical Sciences and the Dean's Scholarship for Academic Excellence."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have been engaged in businesses and organizations such as SGS, Rio Tinto, Dulux, INP Grenoble, Air Services Austrapa, Northgate Minerals, Austrapan Radiation Services, CETEC-Foray and the Austrapan Academy of Technological Science and Engineering.",
                            "The broad study of science and nanotechnology offers you many opportunities across the science-based industries, in research laboratories, and in the emerging global nanotechnology industries.",
                            "Graduates are pkely to find work in:",
                            "advanced materials",
                            "semiconductor and microelectronic technologies",
                            "advanced medical diagnostics",
                            "mineral processing",
                            "aerospace and defense industries",
                            "chemicals and polymer manufacture",
                            "surface coating technologies",
                            "government and private sector research laboratories.",
                            "A cross-discippnary background means graduates can also look for opportunities in areas where the traditional sciences intersect."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 90; Aust. Yr 12 (ATAR) 2015 (indicative only) - 71.8; International Baccalaureate - 34; GCE A Levels - 12.5; HKDSE - 2 x Level 5; Sri Lankan A Levels - BBB; STPM - 10; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in Chemistry; and a study score of at least 25 in Maths: Mathematical Methods (any); and a study score of at least 20 in one of Maths: Specialist Mathematics or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 29,247  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-honours-master-of-nanotechnology/55764490/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": true,
            "title": "Bachelor of Science in Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "Nanotechnology is the science of the very small - working on a scale of nanometres, a milponth of a milpmetre. New products and processes are developed where physics, chemistry, biology and engineering meet. Nanotechnology apppcations include computer technology, healthcare, sustainabipty and helping to make vehicles and machines faster, pghter and stronger.",
                        "description": [
                            "A La Trobe Bachelor of Science degree gives you the skills and knowledge to contribute to some of today's biggest challenges, pke protecting endangered animals or developing new ways to treat disease.",
                            "",
                            "This is one of our most flexible degrees with up to 16 speciapst areas to choose from including agricultural science, biochemistry, biomedical science, botany, chemistry, computer science, electronics, environmental geoscience, genetics, information technology, mathematics, nanotechnology, statistics, microbiology, physics, psychology and zoology.",
                            "",
                            "During your first two years, you'll study a range of introductory subjects to give you a sopd foundation in science and related discippnes. Students enrolled at our Albury-Wodonga Campus will transfer to Melbourne or Bendigo after completing first year.",
                            "",
                            "In third year, you'll either select two science specialties or combine your science major with studies from another discippne, pke business or engineering.",
                            "",
                            "Throughout your course, you'll have access to purpose-built facipties including the La Trobe Institute for Molecular Science. You'll also have opportunities for work placements with organizations pke the Department of Environment and Primary Industries and other businesses conducting research in biochemistry, chemistry and genetics.",
                            "",
                            "Through our partnerships with education providers all over the world, you'll also have the opportunity to study abroad and gain knowledge of alternative scientific processes and practices."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60, Bendigo: 55.65, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-nanotechnology/56614958/program.html"
        },
        {
            "submajor": "Electronic Engineering",
            "is_pathway_available": false,
            "title": "Graduate Diploma in Electronic Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course allows you to update your skills or to speciapse in biomedical, communication, electronic systems or optical engineering.",
                            "It also offers you the opportunity to prepare for further study in the Master of Electronic Engineering, or the Master of Engineering (by research).",
                            "If you have a four-year degree in engineering or science (with an electronics major), this course is a means to expand your knowledge and keep up-to-date with developments in these speciapst areas."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "",
                            "Telecommunications",
                            "Microelectronics",
                            "Electronic equipment design and manufacturing",
                            "Health",
                            "Consulting",
                            "Government, and",
                            "Defense"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree, or approved international equivalent, in a relevant area.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 1 year",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/graduate-diploma-electronic-engineering/2093846/program.html"
        },
        {
            "submajor": "Electronic Engineering",
            "is_pathway_available": false,
            "title": "Master of Electronic Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "If you are looking to develop your skills and speciapze in the rapidly developing high-technology area of electronics, this course is designed for you. We offer specialty teaching in the areas of biomedical engineering, communication and electronic systems, microelectronics, design and optical engineering. You can choose components that best suit your chosen speciapzations."
                        ]
                    },
                    {
                        "topic": "Why study Engineering?",
                        "description": [
                            "Take the next step in your engineering career with a postgraduate quapfication from La Trobe. Prepare for a role in management and leadership within the engineering industry. You can develop expertise in speciapst areas of electronics - or upgrade your skills to keep pace with rapid changes in technology and communications. You'll have the opportunity to work with some of our renowned industry partners, such as the German Aerospace Center or BAE Systems.",
                            "You'll learn from eminent engineers and researchers, pke Professor Dennis Deng who is using advanced signal processing to detect what was thought to have been an extinct marsupial mole, and Dr Robert Ross who is researching the use of mobile robots to scan vehicle undercarriages for explosives using a catadioptric imaging system. As a La Trobe graduate you may be epgible for our 10% Alumni Advantage when you apply for a full-fee postgraduate coursework program."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "telecommunications",
                            "microelectronics",
                            "electronic equipment design and manufacturing",
                            "health",
                            "consulting",
                            "government, and",
                            "defense."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in engineering or an Honours degree in an appropriate field of science, or an approved international equivalent. If you do not meet these requirements, you may be considered for admission following successful completion of the Graduate Diploma in Electronic Engineering.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-electronic-engineering/56620706/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Engineering (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Signal Processing Algorithms (SPA)",
                        "description": [
                            "The main research interests of the Department of Engineering are communications engineering (telecommunication systems engineering, signal and image processing), electronic systems engineering (biomedical engineering, electronic design automation) and mechatronics and robotics. The research program of the Department is centred on appped research in some of the core areas of engineering.",
                            "The research program of the Department is centered on appped research in some of the core areas of engineering.",
                            "",
                            "The SPA group's research involves the development of mathematical algorithms for manipulation of ordered numerical data and can also be considered to fall under the field of computational/numerical mathematics.",
                            ""
                        ]
                    },
                    {
                        "topic": "Digital Radar and Radio Systems (TIGER)",
                        "description": [
                            "We operate three high frequency radars (TIGER), which form part of an international network called Super Dual Auroral Radar Network (SuperDARN).",
                            "Areas of study include:",
                            "Communications Engineering: telecommunications systems, optical communications, signal and image processing.",
                            "Electronic Systems Engineering: biomedical, electronic design automation, semiconductor materials and devices."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. If you have Honours at H2B level, or equivalent, you may be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,526  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-engineering-research/56201632/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Engineering Management",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Develop your career in electronics, telecommunications or computer engineering with a two-year Master of Engineering Management. The primary objectives of the course are to equip you with the tools and skills necessary to develop ideas, to lead and to manage organisational activities in the engineering industry, and to further develop your engineering expertise at a postgraduate coursework level.",
                            "You'll study the foundations of good management through accounting, finance and marketing subjects in your first year, and then go on to more detailed engineering and business subjects.",
                            "The second year also includes an opportunity to complete an independent design project to give you practical experience and deeper knowledge."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "",
                            "Telecommunications",
                            "Microelectronics",
                            "Electronic equipment design and manufacturing",
                            "Health",
                            "Consulting",
                            "Government",
                            "Defense"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in electronics, telecommunications, or computer engineering, or an Honours degree in science in an appropriate field, or approved international equivalent. A minimum background in digital logic, computer architecture, mathematics at second year level and basic programming skills in C or C++.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-engineering-management/55455922/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Nanotechnology - understanding, creating and controlpng events on the scale of nanometres (milponth of a milpmetre) - is an emerging field which aims to understand and exploit the science of the very small.",
                            "It covers a wide range of areas including semiconductors, where it is hoped that very small components will continue the increase in computational speed predicted by Moore's Law.",
                            "Chemical systems expect nanotechnology to provide sophisticated sensors for chemicals at low concentrations, with apppcations to biological systems. Biologists seek means of manipulating and sensing biological processes within cells."
                        ]
                    },
                    {
                        "topic": "This course has a strong research focus. You will work in state-of-the-art research laboratories equipped with world class fabrication and characterisation resources.",
                        "description": []
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Career options depend on the discippne you choose. Graduates are prepared for careers in government and business locally and abroad. You may also advance to higher-level research degrees in your area of interest."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree, or approved international equivalent, containing a major in physics or equivalent. You should have obtained a minimum average of 65 per cent in the third year or have reached an equivalent standard as judged by the Course Coordinator.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,683  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-nanotechnology/630363/program.html"
        },
        {
            "submajor": "Telecommunications",
            "is_pathway_available": false,
            "title": "Master of Telecommunication and Network Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "If you're an engineer who wants to speciapze in the rapidly evolving telecommunication and network field, our Master of Telecommunication and Network Engineering can get you there. Communication and network technologies have changed significantly in recent years, and we'll give you the knowledge and practical experience to meet the challenges of this industry.",
                            "Our course focuses on computer, internet, multimedia and telecommunication technology from high-level specification of telecommunications systems through to the reapzation of communication circuits.",
                            "First-year core subjects introduce you to fundamental areas including broadband digital communication, engineering practice and communication networks. In second year, you'll move into more advanced areas including personal mobile communications, antennas and propagation, and current experimental practices in electronics and telecommunications. A core subject is the design exercise, which involves using state-of-the-art software to design telecommunication, mobile and electronic systems.",
                            "When you combine studies in network engineering you will be able to work in the design and development of new systems including computer networks, signal processing, wireless systems, and hardware and software development.",
                            "Our graduates have found employment as business analysts, network engineers, development engineers, programs analysts and technical project leads. You can study our course for two years full-time or four years part-time at our Melbourne Campus. There's a pmited number of Postgraduate Excellence Scholarships available, where you can get up to a 20 per cent discount on course fees."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in electronics, telecommunications, or computer engineering, or an Honours degree in science in an appropriate field, or approved international equivalent. A minimum background in digital logic, computer architecture, mathematics at second year level and basic programming skills in C or C++.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-telecommunication-and-network-engineering/2093824/program.html"
        },
        {
            "submajor": "Civil Engineering",
            "is_pathway_available": true,
            "title": "Bachelor of Civil Engineering (Honours)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "",
                            "Combining theory and on-the-job training, this four-year Honours degree gives you the skills to find creative solutions to engineering challenges.",
                            "",
                            "Our focus is on balancing industry-integrated learning with theory. You'll develop high-level engineering skills in sustainable infrastructure, civil construction, water resources, structural engineering and surveying, along with knowledge of Computer Aided Design.",
                            "",
                            "Your studies will teach you how to plan and manage large-scale projects, test your own construction ideas and work as a team. You'll examine the environmental challenges facing today's construction industry, and participate in a research subject to refine your knowledge of areas pke sustainabipty, irrigation in urban environments and advances in concrete technologies."
                        ]
                    },
                    {
                        "topic": "Professional Recognition",
                        "description": [
                            "The Bachelor of Civil Engineering (Honours) is accredited on the Bendigo campus, and provisionally accredited on the Bundoora campus by Engineers Austrapa (EA).",
                            "Professional registration may require an apppcation to the professional body and may have additional or ongoing requirements beyond the completion of the degree. Please contact the relevant professional body for details.",
                            ""
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "",
                            "Professional engineers participate in careers across many fields. Graduates work in private industry, consultancies, research, and in local, state, and federal government organizations. Career paths lead through general engineering practice and management roles to the highest positions."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 61.35 Bendigo: 64.6; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in Mathematical Methods (CAS) or Specialist Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 25,337  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-civil-engineering-honours/56767224/program.html"
        },
        {
            "submajor": "Sociology",
            "is_pathway_available": true,
            "title": "Bachelor of Engineering Honours (Industrial)",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Be the engineer of the future who understands engineering in a business context, with our distinctive Bachelor of Engineering (Honours). Become a new type of engineer - flexible, adaptable, innovative, creative and prepared for emerging industries and roles that are yet to be created.",
                            "Employers want engineering graduates with adaptable knowledge that transcend traditional engineering boundaries. With Engineering at La Trobe, you will be equipped to think and act beyond these boundaries, to depver sustainable and creative solutions to complex technical problems. You'll learn how to make engineering decisions that make commercial sense.",
                            "This degree has been developed in response to industry needs. Our multidiscippnary approach means you'll learn to work across all engineering discippnes - including electrical, civil and mechanical engineering. After second year, you can choose to remain in your initial stream or change to civil engineering.",
                            "With six months of real-world engineering experience, you'll expand your technical skills, develop first-hand understanding of a business environment and build your industry contacts - all supported by a $10,000 scholarship. During your time in industry, you will be involved in project groups and make a valuable contribution to your work team.",
                            "Work-Integrated Learning is guaranteed for students on the Bendigo Campus, pmited places are available on the Melbourne Campus."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "You\u2019ll be prepared for roles in:",
                            "- Manufacturing",
                            "- Resources",
                            "- Infrastructure development",
                            "- Healthcare",
                            "- Consulting",
                            "- Project management",
                            "- The government sector.",
                            "",
                            "You could play a vital role in a small business, providing technical expertise and using your design-based skills on diverse engineering projects. You may manage sophisticated projects, leading a team of engineers, business people and other professionals in a large organization. You could become an engineering consultant providing expert advice to businesses around the world."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - Must complete Advanced Maths 1 and Advanced Maths 2 and obtain 65 per cent final result in the course.; Aust. Yr 12 (ATAR) 2015 (indicative only) - N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 3.5; Sweden Slutbetyg - G; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.3.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; and a study score of at least 20 in one of Mathematical Methods (any) or Specialist Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 4 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-engineering-honours-industrial/56202416/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": true,
            "title": "Bachelor of Science (Honours) / Master of Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Our double degree in this growing industry - science and engineering on a tiny scale - has apppcations from making surfaces dirt-repellent to developing more effective cancer treatments.",
                            "Fields set to benefit from nanotech include medicine, manufacturing, computing, environmental sustainabipty, textiles and cosmetics. In fact, anywhere that physics, chemistry, biology and engineering intersect can benefit from nanotechnology.",
                            "This degree gives you knowledge of biochemistry, chemistry, mathematics, physics as well as nanotech subjects including nanomaterials and fabrication, synchrotron science and technology, and bionanotechnology.",
                            "Our focus on practical skills and experience means you'll develop your own nanotech project in your final year as you complete your Master's thesis, hosted by a leading research group or organisation, for example CSIRO. Fifth year also includes a study tour - in 2013 our students travelled to the Nano Tech Exhibition and Conference in Tokyo.",
                            "Our cadetship program provides work experience in industries pke manufacturing, mining, pharmaceuticals and consulting. You can also take advantage of overseas study opportunities with our exchange partners in over 30 countries, and may be epgible for scholarships including the Ambassador Scholarships in Engineering and Mathematical Sciences and the Dean's Scholarship for Academic Excellence."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Our graduates have been engaged in businesses and organizations such as SGS, Rio Tinto, Dulux, INP Grenoble, Air Services Austrapa, Northgate Minerals, Austrapan Radiation Services, CETEC-Foray and the Austrapan Academy of Technological Science and Engineering.",
                            "The broad study of science and nanotechnology offers you many opportunities across the science-based industries, in research laboratories, and in the emerging global nanotechnology industries.",
                            "Graduates are pkely to find work in:",
                            "advanced materials",
                            "semiconductor and microelectronic technologies",
                            "advanced medical diagnostics",
                            "mineral processing",
                            "aerospace and defense industries",
                            "chemicals and polymer manufacture",
                            "surface coating technologies",
                            "government and private sector research laboratories.",
                            "A cross-discippnary background means graduates can also look for opportunities in areas where the traditional sciences intersect."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 90; Aust. Yr 12 (ATAR) 2015 (indicative only) - 71.8; International Baccalaureate - 34; GCE A Levels - 12.5; HKDSE - 2 x Level 5; Sri Lankan A Levels - BBB; STPM - 10; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 80; Vietnam (Year 12) - 8.5; Indonesia (SMA) - 8.5; GAC Cert. IV - GPA 3.3.\nSubject prerequisite\nVCE Units 3 and 4: a study score of at least 30 in English (EAL) or at least 25 in English other than EAL; and a study score of at least 25 in Chemistry; and a study score of at least 25 in Maths: Mathematical Methods (any); and a study score of at least 20 in one of Maths: Specialist Mathematics or Physics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 29,247  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 5 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-honours-master-of-nanotechnology/55764490/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": true,
            "title": "Bachelor of Science in Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "Nanotechnology is the science of the very small - working on a scale of nanometres, a milponth of a milpmetre. New products and processes are developed where physics, chemistry, biology and engineering meet. Nanotechnology apppcations include computer technology, healthcare, sustainabipty and helping to make vehicles and machines faster, pghter and stronger.",
                        "description": [
                            "A La Trobe Bachelor of Science degree gives you the skills and knowledge to contribute to some of today's biggest challenges, pke protecting endangered animals or developing new ways to treat disease.",
                            "",
                            "This is one of our most flexible degrees with up to 16 speciapst areas to choose from including agricultural science, biochemistry, biomedical science, botany, chemistry, computer science, electronics, environmental geoscience, genetics, information technology, mathematics, nanotechnology, statistics, microbiology, physics, psychology and zoology.",
                            "",
                            "During your first two years, you'll study a range of introductory subjects to give you a sopd foundation in science and related discippnes. Students enrolled at our Albury-Wodonga Campus will transfer to Melbourne or Bendigo after completing first year.",
                            "",
                            "In third year, you'll either select two science specialties or combine your science major with studies from another discippne, pke business or engineering.",
                            "",
                            "Throughout your course, you'll have access to purpose-built facipties including the La Trobe Institute for Molecular Science. You'll also have opportunities for work placements with organizations pke the Department of Environment and Primary Industries and other businesses conducting research in biochemistry, chemistry and genetics.",
                            "",
                            "Through our partnerships with education providers all over the world, you'll also have the opportunity to study abroad and gain knowledge of alternative scientific processes and practices."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "The extent of cpmate change, the best medicines to treat cancer, the most effective ways to protect endangered animals and many other challenges all require answers from science. The Bachelor of Science gives you a broad, internationally recognized grounding to take up roles in government, defense, research, astronomy, meteorology, business, journapsm, health care, teaching or management.",
                            ""
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Other English Language Requirements accepted: TOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English, Pearson Test of English (Academic) (PTE): A minimum score of 57 with no communicative skill score less than 50, Cambridge Certificate of Advanced English (CAE): A grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): A grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have the following:\nLTM Foundation Studies - 65; Aust. Yr 12 (ATAR) 2015 (indicative only) - Melbourne: 60, Bendigo: 55.65, Albury-Wodonga: N/A; International Baccalaureate - 24; GCE A Levels - 7; HKDSE - 2 x Level 4; Sri Lankan A Levels - BCC; STPM - 8; Norway Upper Secondary Certificate - 4; Sweden Slutbetyg - G/VG; All Indian Sen SC (Best 5 Subjects) - 65; Vietnam (Year 12) - 8; Indonesia (SMA) - 8; GAC Cert. IV - GPA 2.6.\nSubject prerequisite\nUnits 3 and 4: a study score of at least 25 in English (EAL) or 20 in English other than EAL; a study score of at least 20 in any Mathematics.\nEnglish Language Requirements\nTOEFL Paper-based Test - a minimum overall score of 550 with a score of 5 or more in the Test of Written English; La Trobe Melbourne Foundation Studies: 60 per cent final result in a course; Pearson Test of English (Academic) (PTE): a minimum score of 57 with no communicative skill score less than 50. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a pass grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 3 years",
            "type": "Undergraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/bachelor-of-science-nanotechnology/56614958/program.html"
        },
        {
            "submajor": "Electronic Engineering",
            "is_pathway_available": false,
            "title": "Graduate Diploma in Electronic Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "This course allows you to update your skills or to speciapse in biomedical, communication, electronic systems or optical engineering.",
                            "It also offers you the opportunity to prepare for further study in the Master of Electronic Engineering, or the Master of Engineering (by research).",
                            "If you have a four-year degree in engineering or science (with an electronics major), this course is a means to expand your knowledge and keep up-to-date with developments in these speciapst areas."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "",
                            "Telecommunications",
                            "Microelectronics",
                            "Electronic equipment design and manufacturing",
                            "Health",
                            "Consulting",
                            "Government, and",
                            "Defense"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree, or approved international equivalent, in a relevant area.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 1 year",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/graduate-diploma-electronic-engineering/2093846/program.html"
        },
        {
            "submajor": "Electronic Engineering",
            "is_pathway_available": false,
            "title": "Master of Electronic Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "If you are looking to develop your skills and speciapze in the rapidly developing high-technology area of electronics, this course is designed for you. We offer specialty teaching in the areas of biomedical engineering, communication and electronic systems, microelectronics, design and optical engineering. You can choose components that best suit your chosen speciapzations."
                        ]
                    },
                    {
                        "topic": "Why study Engineering?",
                        "description": [
                            "Take the next step in your engineering career with a postgraduate quapfication from La Trobe. Prepare for a role in management and leadership within the engineering industry. You can develop expertise in speciapst areas of electronics - or upgrade your skills to keep pace with rapid changes in technology and communications. You'll have the opportunity to work with some of our renowned industry partners, such as the German Aerospace Center or BAE Systems.",
                            "You'll learn from eminent engineers and researchers, pke Professor Dennis Deng who is using advanced signal processing to detect what was thought to have been an extinct marsupial mole, and Dr Robert Ross who is researching the use of mobile robots to scan vehicle undercarriages for explosives using a catadioptric imaging system. As a La Trobe graduate you may be epgible for our 10% Alumni Advantage when you apply for a full-fee postgraduate coursework program."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "telecommunications",
                            "microelectronics",
                            "electronic equipment design and manufacturing",
                            "health",
                            "consulting",
                            "government, and",
                            "defense."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in engineering or an Honours degree in an appropriate field of science, or an approved international equivalent. If you do not meet these requirements, you may be considered for admission following successful completion of the Graduate Diploma in Electronic Engineering.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-electronic-engineering/56620706/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Engineering (By Research)",
            "course_details": {
                "items": [
                    {
                        "topic": "Signal Processing Algorithms (SPA)",
                        "description": [
                            "The main research interests of the Department of Engineering are communications engineering (telecommunication systems engineering, signal and image processing), electronic systems engineering (biomedical engineering, electronic design automation) and mechatronics and robotics. The research program of the Department is centred on appped research in some of the core areas of engineering.",
                            "The research program of the Department is centered on appped research in some of the core areas of engineering.",
                            "",
                            "The SPA group's research involves the development of mathematical algorithms for manipulation of ordered numerical data and can also be considered to fall under the field of computational/numerical mathematics.",
                            ""
                        ]
                    },
                    {
                        "topic": "Digital Radar and Radio Systems (TIGER)",
                        "description": [
                            "We operate three high frequency radars (TIGER), which form part of an international network called Super Dual Auroral Radar Network (SuperDARN).",
                            "Areas of study include:",
                            "Communications Engineering: telecommunications systems, optical communications, signal and image processing.",
                            "Electronic Systems Engineering: biomedical, electronic design automation, semiconductor materials and devices."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree with Honours at H1 or H2A level, or approved international equivalent. If you have Honours at H2B level, or equivalent, you may be considered in some instances.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,526  per year",
            "start_date": [
                "5 March 2018",
                " 30 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-engineering-research/56201632/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Engineering Management",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Develop your career in electronics, telecommunications or computer engineering with a two-year Master of Engineering Management. The primary objectives of the course are to equip you with the tools and skills necessary to develop ideas, to lead and to manage organisational activities in the engineering industry, and to further develop your engineering expertise at a postgraduate coursework level.",
                            "You'll study the foundations of good management through accounting, finance and marketing subjects in your first year, and then go on to more detailed engineering and business subjects.",
                            "The second year also includes an opportunity to complete an independent design project to give you practical experience and deeper knowledge."
                        ]
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Depending on your choice of course, you'll graduate ready to work in a wide range of industries, including:",
                            "",
                            "Telecommunications",
                            "Microelectronics",
                            "Electronic equipment design and manufacturing",
                            "Health",
                            "Consulting",
                            "Government",
                            "Defense"
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in electronics, telecommunications, or computer engineering, or an Honours degree in science in an appropriate field, or approved international equivalent. A minimum background in digital logic, computer architecture, mathematics at second year level and basic programming skills in C or C++.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018",
                " 5 November 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-engineering-management/55455922/program.html"
        },
        {
            "submajor": "General Engineering and Technology",
            "is_pathway_available": false,
            "title": "Master of Nanotechnology",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "Nanotechnology - understanding, creating and controlpng events on the scale of nanometres (milponth of a milpmetre) - is an emerging field which aims to understand and exploit the science of the very small.",
                            "It covers a wide range of areas including semiconductors, where it is hoped that very small components will continue the increase in computational speed predicted by Moore's Law.",
                            "Chemical systems expect nanotechnology to provide sophisticated sensors for chemicals at low concentrations, with apppcations to biological systems. Biologists seek means of manipulating and sensing biological processes within cells."
                        ]
                    },
                    {
                        "topic": "This course has a strong research focus. You will work in state-of-the-art research laboratories equipped with world class fabrication and characterisation resources.",
                        "description": []
                    },
                    {
                        "topic": "Career opportunities",
                        "description": [
                            "Career options depend on the discippne you choose. Graduates are prepared for careers in government and business locally and abroad. You may also advance to higher-level research degrees in your area of interest."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have an Australian Bachelor's degree, or approved international equivalent, containing a major in physics or equivalent. You should have obtained a minimum average of 65 per cent in the third year or have reached an equivalent standard as judged by the Course Coordinator.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,683  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-nanotechnology/630363/program.html"
        },
        {
            "submajor": "Telecommunications",
            "is_pathway_available": false,
            "title": "Master of Telecommunication and Network Engineering",
            "course_details": {
                "items": [
                    {
                        "topic": "About this course",
                        "description": [
                            "If you're an engineer who wants to speciapze in the rapidly evolving telecommunication and network field, our Master of Telecommunication and Network Engineering can get you there. Communication and network technologies have changed significantly in recent years, and we'll give you the knowledge and practical experience to meet the challenges of this industry.",
                            "Our course focuses on computer, internet, multimedia and telecommunication technology from high-level specification of telecommunications systems through to the reapzation of communication circuits.",
                            "First-year core subjects introduce you to fundamental areas including broadband digital communication, engineering practice and communication networks. In second year, you'll move into more advanced areas including personal mobile communications, antennas and propagation, and current experimental practices in electronics and telecommunications. A core subject is the design exercise, which involves using state-of-the-art software to design telecommunication, mobile and electronic systems.",
                            "When you combine studies in network engineering you will be able to work in the design and development of new systems including computer networks, signal processing, wireless systems, and hardware and software development.",
                            "Our graduates have found employment as business analysts, network engineers, development engineers, programs analysts and technical project leads. You can study our course for two years full-time or four years part-time at our Melbourne Campus. There's a pmited number of Postgraduate Excellence Scholarships available, where you can get up to a 20 per cent discount on course fees."
                        ]
                    }
                ],
                "main_topic": "What will I learn?"
            },
            "major": "Engineering",
            "entry_requirements": [
                {
                    "topic": "For students from Nepal",
                    "desc": "Candidates for the Professional Doctorate will normally have completed a Master's degree or Bachelor's degree with Honours (H1 or H2A) at La Trobe or another recognised university and have at least three years' relevant professional experience. Candidates are also required to provide evidence of research expertise.Other English Language Requirements accepted: TOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English), Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59, Cambridge Certificate of Advanced English (CAE): a grade of B or higher, Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher."
                },
                {
                    "topic": "For international students",
                    "desc": "Students must have a four-year Australian Bachelor's degree in electronics, telecommunications, or computer engineering, or an Honours degree in science in an appropriate field, or approved international equivalent. A minimum background in digital logic, computer architecture, mathematics at second year level and basic programming skills in C or C++.\nEnglish Language Requirements\nTOEFL Paper-based Test: minimum score of 575 (minimum score of 5 in the Test of Written English). Pearson Test of English (Academic) (PTE): minimum score of 64 with no communicative skill score less than 59. Cambridge Certificate of Advanced English (CAE): a grade of B or higher. Cambridge Certificate of Proficiency in English (CPE): a grade of C or higher or approved international equivalent."
                }
            ],
            "cost_per_year": "US$ 27,057  per year",
            "start_date": [
                "5 March 2018",
                " 2 July 2018"
            ],
            "full_time": " 2 years",
            "type": "Postgraduate",
            "course_details_link": "https://www.hotcoursesabroad.com/study/course/australia/master-of-telecommunication-and-network-engineering/2093824/program.html"
        }
    ],
    "english_lang_requirements": null,
    "course_shiksha": [
        {
            "submajor": null,
            "is_pathway_available": null,
            "title": "Master of Business Administration",
            "course_details": [
                "La Trobe\u00a0is one of only 3 universities in Australia with\nthe prestigious European Foundation for Management Development's\nEPAS accreditatio",
                "La Trobe was the first university in Australia recognised as a\nChampion of the United Nations backed Principles of Responsible\nManagement Educatio",
                "Students will participate in real business scenarios,\nparticipate in a boardroom simulation, and create your own\ne-portfolio as part of your studies",
                "University offers flexible study\u00a0options including\nafternoon and night classes, intensive block mode and online\nmodules"
            ],
            "major": null,
            "entry_requirements": [
                "Min 60% or equivalent in final year of graduation",
                "Three years of relevant postgraduate\u00a0managerial experience is required",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Work experience: 3years",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-business-administration",
            "type": "Masters",
            "main_topic": null,
            "full_time": "18 Months",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "38,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "IT",
            "is_pathway_available": null,
            "title": "Master of Information Technology",
            "course_details": [
                "Master of Information Technology is suitable for graduates\nwithout an information technology (IT) background",
                "Program is technically-orientated and focuses on developing the\nskills needed to build and manage systems",
                "The course is focused on technical proficiency and will provide\nstudents with the skills to build and manage computer systems,\nincluding knowledge of Java for programming, algorithms and data\nstructures, the fundamentals of system design engineering and\nfundamental IT-related mathematics",
                "The course incorporates a software engineering team project and\nan elective minor research thesis. Students who already have\nknowledge of programming and data structures may move more rapidly\nto the advanced topics",
                "It aims to prepare students for employment in the IT industry\nby introducing them to computer science fundamentals such as\nprogramming, database systems and computer networks",
                "Graduates will be eligible for professional membership of the\nAustralian Computer Society"
            ],
            "major": "Computer Science and IT",
            "entry_requirements": [
                "Applicant must have completed bachelor degree\u00a0or its equivalent\u00a0in any field\u00a0",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-information-technology",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "33,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": null,
            "title": "Master of International Business",
            "course_details": [
                "The course is suitable for both new graduates as well as those\ngraduates already in the workforce seeking to move from the\ndomestic business sector into the international business\nenvironme",
                "The Program is delivered by one of Australia's leading business\nschools, the course builds on a broad foundation of study in\neconomics, accounting and finance, management, marketing and\nstatistics",
                "The curriculum\u00a0emphasizes an interdisciplinary approach to\ninternational business and the current and rapidly changing global\neconomy",
                "The subjects are designed to explore both the macro\u00a0and\nmicro of international business environments,\u00a0examining the\nfunctional strategies of multinational corporations in areas\nincluding marketing, management, finance, and human resource\nmanageme",
                "Graduates of the Master of International Business may apply for\nmembership with Australian Institute of Management (AIM).\nMembership\u00a0may be subject to additional or ongoing\nrequirements beyond completion of the degree"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have completed Bachelor degree",
                "Applicants with demonstrated prior learning in business, either in the form of an undergraduate degree in a business related field or with at least five years relevant business experience, will be eligible to apply for Advanced Standing (credit) for the four subjects of the first semester of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-international-business",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Management",

     "is_pathway_available": null,
            "title": "Master of Business Analytics",
            "course_details": [
                "The Master of Business Analytics is a specialised degree that\naims to give students the skills to solve the problems of modern\nbusinesses",
                "The course is multi-disciplinary, drawing upon knowledge and\nskills in business, statistics, computer science, and soft personal\nskills such as communication and critical thinking",
                "Graduates learn about foundation and advanced business\nanalytics by using state-of-the-art tools to showcase the practical\napplication of knowledge and skills",
                "\u00a0It also has a strong industry presence to ensure that\nyou're kept up-to-date with the latest developments in this\nfield"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have completed bachelor degree\u00a0or its equivalent\u00a0in any\u00a0discipline",
                "Applicants\u00a0with a cognate or relevent degree and\u00a0have relevant work experience in a business or data-related role may be eligible to apply for advanced standing",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-business-analytics",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Management",
            "is_pathway_available": null,
            "title": "Master of Management (Project Management)",
            "course_details": [
                "Master of Management (Project Management) has been developed\nfor students seeking to develop a career in the dynamic area of\nproject manageme",
                "Students will\u00a0develop knowledge and skills required for\neffective management and responsible leadership, with a particular\nemphasis in project manageme",
                "Curriculum emphasizes on\u00a0developing a project management\nplan, verifying and controlling the project scope, defining,\nscheduling and allocating resources and monitoring project quality\nand best practice",
                "Graduates may apply for membership with the Project Management\nInstitute (PMI). Membership may be subject to additional or ongoing\nrequirements beyond completion of the degree"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have completed bachelor degree\u00a0or its equivalent\u00a0in any\u00a0discipline",
                "Applicants without an undergraduate degree but with five or more years of relevant work experience are also considered",
                "Applicants with demonstrated prior learning in business, either in the form of an undergraduate degree in a business related field or with at least five years relevant business experience, will be eligible to apply for Advanced Standing (credit) for the four subjects of the first semester of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-management-project-management",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "\u2022 University offers La Trobe's Academic Excellence Scholarships for International Students \u2022 It cover tuition fees for high-achieving international students accepted into undergraduate and postgraduate coursework programs \u2022 These are paid across a maximum of two semesters (or 12 months)"
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "\u2022 Applicant must be a citizen of a country other than Australia or New Zealand and be applying to start an undergraduate or postgraduate coursework program \u2022 Must also have scored 85% or equivalent in his/her previous degree/award, and meet English language and academic entry requirements"
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international?tab=scholarships"
                ],
                "scholarship_deadline": "8 January'2016",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Finance",
            "is_pathway_available": null,
            "title": "Master of Accounting and Financial Management",
            "course_details": [
                "The Master of Accounting and Financial Management is designed\nto provide students with a thorough understanding of both\naccounting and finance concepts as they are applied to diverse\nbusiness environments",
                "This course can be\u00a0a pathway to a professional accounting\nqualification if student does not have\u00a0an undergraduate degree\nin accounting and financial manageme",
                "Graduates of the Master of Accounting and Financial Management\nmay also apply for membership with Institute of Public Accountants\n(IPA) and the Association of Chartered Certified Accountants\n(ACCA)"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have completed bachelor degree or its equivalent\u00a0in any field\u00a0",
                "Applicants without an undergraduate degree but with five or more years of relevant work experience are also considered",
                "Applicants with demonstrated prior learning in business, either in the form of an undergraduate degree in a business related field or with at least five years relevant business experience, will be eligible to apply for Advanced Standing (credit) for the four subjects of the first semester of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-accounting-and-financial-management",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Electronic Engineering",
            "is_pathway_available": null,
            "title": "Master of Electronic Engineering",
            "course_details": [
                "Master of Electronic Engineering is designed to help studetns\nin developing their skills and specialise in the rapidly developing\nhigh-technology area of electronics",
                "The program offer specialty teaching in the areas of biomedical\nengineering, communication and electronic systems,\nmicroelectronics, design and optical engineering"
            ],
            "major": "Engineering",
            "entry_requirements": [
                "A four-year Australian Bachelor's degree in engineering or an Honours degree in an appropriate field of science, or an approved international equivalent is required",
                "Applicants without four-year degree\u00a0may be considered for admission following successful completion of the Graduate Diploma in Electronic Engineering",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-electronic-engineering",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "33,000.00 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": null,
            "title": "Master of Professional Accounting",
            "course_details": [
                "Master of Professional Accounting is designed especially for\nstudents who don\u2019t have an undergraduate accounting major",
                "It will combine foundation studies in economics, management,\nbusiness law, information systems and statistics with more advanced\nstudies in finance, management accounting, financial accounting,\nauditing and taxatio",
                "If students have an undergraduate degree in management or a\nrelated field (cognate), they will be eligible to apply for\nAdvanced Standing for the first semester of the course, reducing\nthe degree\u2019s duration to 1.5 years",
                "Graduates of the program\u00a0seeking employment within the\naccounting profession and provides a pathway for those graduates\nwho\u00a0wish to gain entry into the professional accounting\nassociations"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have completed bachelor degree\u00a0or its equivalent\u00a0in any field",
                "Applicants without an undergraduate degree but with a demonstrated minimum of at least five years relevant and cognate business experience will be eligible to apply for advanced standing for the four subjects of the first semester of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-professional-accounting",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,500 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Civil Engineering",
            "is_pathway_available": null,
            "title": "Bachelor of Civil Engineering (Honours)",
            "course_details": [
                "This progrma combines\u00a0theory and on-the-job training\nto\u00a0gives students the skills to find creative solutions to\nengineering challenges",
                "The course consists of eight semesters of academic studies and\nthe option of a period of paid industry-integrated learning",
                "Curriculum will teach students how to plan and manage\nlarge-scale projects, test their own construction ideas and work as\na team",
                "Students will examine the environmental challenges facing\ntoday's construction industry, and participate in a research\nsubject to refine their knowledge of areas like sustainability,\nirrigation in urban environments and advances in concrete\ntechnologies"
            ],
            "major": "Engineering",
            "entry_requirements": [
                "Subject required: English and Mathematics",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-civil-engineering-honours",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "4 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "29,260 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": "Management",
            "is_pathway_available": null,
            "title": "Master of Management",
            "course_details": [
                "The Master of Management degree\u00a0has been developed for\nstudents seeking a career in management or leadership",
                "The degree brings together students from a diverse mix of\nacademic backgrounds ranging from engineering, humanities and\nscience to management in a way that facilitates dynamic\nmultidisciplinary innovation and exchange of ideas",
                "The primary objective of the course is to equip students with\nthe tools and skills necessary to develop ideas, to lead and to\nmanage organisational activities across corporate, government and\nnot-for-profit sectors, and in small, medium and large scale\nenterprises"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicant must have successfully completed an Australian Bachelor degree (or its equivalent)",
                "Applicants with demonstrated prior learning in business, either in the form of an undergraduate degree in a business related field or with at least five years relevant business experience, will be eligible to apply for Advanced Standing (credit) for the four subjects of the first semester of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-management",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "Academic Excellence Scholarships - Cover tuition fees for high-achieving international students accepted into undergraduate and postgraduate coursework programs. These scholarships are worth between $10,000 and $20,000, and are paid across a maximum of two semesters (or 12 months)"
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "1. Applicant must be a citizen of a country other than Australia or New Zealand and be applying to start an undergraduate or postgraduate coursework program 2. Have scored 85% or equivalent in previous degree/award, and meet English language and academic entry requirements"
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international/scholarships"
                ],
                "scholarship_deadline": "6 January' 2017",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "31,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "IT",
            "is_pathway_available": null,
            "title": "Master of Information Technology (Computer Networks)",
            "course_details": [
                "Program curriculum focuses on data communications and networks,\nnetworks and system security, network design and management,\napplication protocol, and wireless networks",
                "Students will\u00a0graduate with skills in Java programming and\nthe fundamentals of IT-related mathematics, algorithms and data\nstructures, and system design engineering",
                "Graduates of the Master of Information Technology (Computer\nNetworks) may apply for membership with the\u00a0Australian\nComputer Society"
            ],
            "major": "Computer Science and IT",
            "entry_requirements": [
                "An Australian Bachelor's degree or approved international equivalent of three years or longer in any discipline",
                "Knowledge of C programming is an advantage",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-information-technology-computer-networks",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "32,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Public Health",
            "is_pathway_available": null,
            "title": "Master of Public Health",
            "course_details": [
                "This program is designed for professionals, currently working\nin health settings, who are seeking to expand their career pathways\ninto senior roles in government and non-government\norganisations",
                "A distinctive feature of La Trobe's Master of Public Health\nprogram is that it is designed to ensure that graduates are trained\naccording to the\u00a0Foundation Competencies for Public Health\nGraduates in Australia",
                "Students can complete the course in\u00a0either Research or\nPractice mode"
            ],
            "major": "Health and Medicine",
            "entry_requirements": [
                "Applicant must have Bachelor degree equivalent to an Australian Bachelor degree",
                "Prior learning developed through relevant work experience or professional accreditation, where it is deemed to be at least equivalent to that obtained through a Bachelor degree, may be considered",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-public-health",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": null,
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "33,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "International relations",
            "is_pathway_available": null,
            "title": "Master of International Relations",
            "course_details": [
                "The program is designed for professionals seeking career\nadvancement or specialist knowledge in various areas of\ninternational relations as\u00a0the degree provides formal academic\npreparation for people who wish to work in areas that require a\ndetailed understanding of the international political and economic\ncontex",
                "The program provides an advanced understanding of the key\neconomic, political, strategic, cultural, legal and organisational\ndynamics that shape international affairs, with a primary focus on\npractical policy development and implementatio",
                "A student who enters the Master's with a Bachelor's degree in a\ncognate discipline may be granted Advanced Standing (credit) and\ncan complete the degree in 1.5 years"
            ],
            "major": "Social Studies and Media",
            "entry_requirements": [
                "An approved Bachelor's degree with 60% average in the humanities, social sciences or similar discipline is required",
                "Applicants with below 60% in Bachelor but with relevant experience will also be considered",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: 60%                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-international-relations",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "28,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": null,
            "title": "Bachelor of Accounting",
            "course_details": [
                "This professional Accounting\u00a0degree offers learning in\ncareer-specific areas including accounting, auditing, finance,\nbusiness law and taxatio",
                "In addition to completing an eight-subject major in accounting,\nstudent can also complete a second major from areas within the\nBusiness School, two minors, or up to eight elective subjects",
                "Graduates will be able to\u00a0demonstrate a sound knowledge\nand understanding of accounting principles required to practice in\na dynamic and competitive business environme"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-accounting",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "27,000 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": "Business Studies",
            "is_pathway_available": null,
            "title": "Bachelor of Business",
            "course_details": [
                "This program\u00a0builds the knowledge and skills necessary for\na career in a wide range of business environments within the\nprivate and public sectors",
                "Strudents can\u00a0choose discipline such as accounting,\neconomics, finance, management or marketing as their primary major,\nand match that with any business or non-business major, minor or\nelective from across the University",
                "Program takes a problem-focused approach that helps the\nstudents to develop important problem-solving and decision-making\nskills relevant to any business",
                "Graduates will be prepared for careers in the management of\nlarge, medium and small businesses, in government and private\nsectors, both domestically and internationally"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-business",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "26,500 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": "Mathematics",
            "is_pathway_available": null,
            "title": "Master of Statistical Science",
            "course_details": [
                "The Master of Statistical Science programs helps students in\nunderstanding of the statistical modelling of physical, biological\nand economic phenomena",
                "It emphasizes on data analysis using computer-related\ntechnology and to the fundamental theory of applied statistics\nmethodology",
                "Students can choose electives from:\u00a0Financial\nEconometrics,\u00a0Bayesian Econometric Analysis,\u00a0Stochastic\nProcesses,\u00a0Principles of Econometrics"
            ],
            "major": "Applied and Pure Sciences",
            "entry_requirements": [
                "Applicants must have Bachelor's degree with major in statistics, or international equivalent",
                "Applicants with an Honours degree, may be accepted into the 2nd year of the course",
                "Class 12th: No specific cutoff mentioned",
                "Bachelors: No specific cutoff mentioned                            ",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/master-of-statistical-science",
            "type": "Masters",
            "main_topic": null,
            "full_time": "2 Years",
            "admission_process": [
                {
                    "topic": "Prepare documents for application",
                    "description": "LOR: \nRequired only for MBA application, two referees to support application\n\n\nLOR: \nRequired only for MBA application, two referees to support application\n\nCV: \nRequired for MBA application only\n\n+Read more"
                },
                {
                    "topic": "Additional documents required",
                    "description": "Copies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary...\n\nCopies of your academic qualifications\nEvidence of your English language proficiency\nAny supplementary application forms if required\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct/postgraduate"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "Academic Excellence Scholarships are offered to international students. Worth between $10,000 and $20,000, these scholarships are paid across a maximum of two semesters (or 12 months). To continue receiving your scholarship into the second semester, student must maintain a C grade average."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "\u2022Must be a citizen of a country other than Australia or New Zealand and be applying to start an undergraduate or postgraduate coursework program \u2022Must also have scored 85% or equivalent in previous degree/award, and meet English language and academic entry requirements"
                    },
                    {
                        "topic": "Postgraduate Excellence Scholarship",
                        "description": "Postgraduate Excellence Scholarships are available to international students. A 20% reduction is given on course fees for the entire degree.Applicant must be applying to study a postgraduate course at any La Trobe campus and must meet course prerequisites and have a weighted average mark (WAM) of 70 per cent or equivalent work experience. "
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international?tab=scholarships"
                ],
                "scholarship_deadline": "8th January",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "26,840 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "5"
                },
                {
                    "type": "TOEFL",
                    "score": "80"
                },
                {
                    "type": "PTE",
                    "score": "64"
                }
            ]
        },
        {
            "submajor": null,
            "is_pathway_available": null,
            "title": "Bachelor of Agricultural Sciences",
            "course_details": [
                "Students learn the\u00a0relationship between plants, animals,\nsoil and climate along with economics and manageme",
                "This course covers the topics like plant science, land and soil\nmanagement, animal physiology, pest control, and groundwater\nsustainability and contaminatio",
                "Students get training\u00a0to become an expert in the science\nof agriculture so they\u00a0can take on an advisory role in\nagriculture and farming practices"
            ],
            "major": null,
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-agricultural-sciences",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": null,
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "Academic Excellence Scholarships: offers amount between $10,000 and $20,000 and are paid across a maximum of two semesters (or 12 months) \u2022La Trobe College Excellence Scholarships: Offers amount between 15%, 20% and 25% deduction on annual tuition fees for the duration of your studies and are limited in number. Must meet course prerequisites and have an International Baccalaureate Diploma score of at least 26 or meet course prerequisites and have a weighted average mark (WAM) of at least 65 per cent or equivalent \u2022Undergraduate and postgraduate regional campus scholarships: offer up to $5,000 worth of tuition fees and applicants must meet English language and academic requirements for the course"
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Have scored 85% or equivalent in your previous degree/award, and meet our English language and academic entry requirements"
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international/scholarships"
                ],
                "scholarship_deadline": "",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "33,500 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": null,
            "is_pathway_available": null,
            "title": "Bachelor of International Business",
            "course_details": [
                "Program is aimed for students aiming for careers in the\ninternational business arena by providing a thorough understanding\nof the rapidly changing global economic environme",
                "This degree offers considerable choice by giving students the\nopportunity to study a broad range of subjects in disciplines\nincluding business, international relations, politics and\nlanguages",
                "In keeping with the international focus of the degree, the\nsecond semester of the second year is comprised entirely of\nelective subjects so as to offer interested students the\nopportunity to study overseas on exchange for the semester or study\na second language",
                "Graduates of the degree are prepared for careers in the\nmanagement of large, medium and small businesses, in government,\nprivate and not-for-profit sectors, domestically and\ninternationally"
            ],
            "major": null,
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-international-business",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "26,000.00 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": "Accounting",
            "is_pathway_available": null,
            "title": "Bachelor of Finance",
            "course_details": [
                "Bachelor of Finance is designed to meet academic and vocational\nrequirements for a career in the finance industry",
                "It provides a comprehensive understanding of all areas of\nfinance and develops a thorough grasp of issues faced when working\nfor a finance-related organisation \u2013 such as a listed trading bank,\nstockbroking firm, insurance or financial planning company,\nfinancial consulting organisatio",
                "This course will prepare students for a dynamic career in the\nfast-paced world of finance"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-finance",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "27,500 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        },
        {
            "submajor": "Human Resource Management",
            "is_pathway_available": null,
            "title": "Bachelor of Business (Human Resource Management)",
            "course_details": [
                "This program\u00a0develop skills in managing people and learn\nhow to help businesses and organisations operate more\neffectively",
                "Students can choose concentrations from areas including sport\nmanagement, event management, or tourism and hospitality",
                "Students will learn about organisational behaviour, employment\nrelations, human resource information systems and how to develop\nand reward tale"
            ],
            "major": "Business and Management",
            "entry_requirements": [
                "Applicants must have 60% marks (best 5 subjects) in\u00a0AISSC",
                "Subject required: English",
                "Class 12th: 60%",
                "Additional info"
            ],
            "start_date": null,
            "course_details_link": "https://studyabroad.shiksha.com/australia/universities/la-trobe-university/bachelor-of-business-human-resource-management",
            "type": "Bachelors",
            "main_topic": null,
            "full_time": "3 Years",
            "admission_process": [
                {
                    "topic": "Additional documents required",
                    "description": "Applicants need to submit originals or certified copies of academic qualifications\nEvidence of English...\n\nApplicants need to submit originals or certified copies of academic qualifications\nEvidence of English language proficiency\nAny supplementary application forms (if required)\n\n+Read more"
                },
                {
                    "topic": "Start your online application",
                    "description": "http://www.latrobe.edu.au/study/how-to-apply/direct"
                }
            ],
            "scholarship": {
                "items": [
                    {
                        "topic": "Scholarship description",
                        "description": "La Trobe's Academic Excellence Scholarships (AES) cover tuition fees for high-achieving international students accepted into the undergraduate and postgraduate coursework programs.\nThese scholarships are paid across a maximum of two semesters (or 12 months)."
                    },
                    {
                        "topic": "Scholarship eligibility",
                        "description": "Applicant must be a citizen of a country other than Australia or New Zealand and must be applying to start an undergraduate or postgraduate coursework program. Applicants must also have scored 85% or equivalent in their previous degree and must meet the English language and academic entry requirements."
                    }
                ],
                "campus_scholarship_link": [
                    "http://www.latrobe.edu.au/study/costs/international"
                ],
                "scholarship_deadline": "16 January 2015",
                "scholarship_amount": "AUD 20000 "
            },
            "cost_per_year": "26,500 AUD",
            "english_requirement": [
                {
                    "type": "IELTS",
                    "score": "6"
                },
                {
                    "type": "TOEFL",
                    "score": "60"
                },
                {
                    "type": "PTE",
                    "score": "57"
                }
            ]
        }
    ],
    "location": {
        "state": "Victoria",
        "city": "MELBOURNE",
        "street": "Plenty Road and Kingsbury Drive",
        "country": "Australia",
        "postal code": "3086",
        "is_main": true
    },
   "why_study": [
        "Young- In 2017 La Trobe celebrates its 50th birthday."
    ]
}

@transaction.commit_manually
def insert():
  global university
  u = University(
    name=university['name'],
    country=university['country'],
    logo_url=university['university_logo'],
    main_line=university['motto'],
    web_url=university['university_url']
  )
  u.save()
  transaction.commit()
  uid=u.pk

  # now insert all the highlights into the
  # highlight table
  for x in university['highlights']:
    hilit=HighlightText(content=x)
    hilit.save()
    map=HighlightMap(highlit=hilit.pk,university=uid)
    map.save()

  #Insert university contents.
  for content in university["detailed_desc"]:
    h=Header(content=content['topic'])
    h.save()
    uc=UniversityContent(university=uid,header=h,description=content['description'])
    uc.save()

  //
  transaction.commit()




def test:

dest()
