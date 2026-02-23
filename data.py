site_data = {
    "name": "Erica Babusci",
    "title": "PhD Candidate — Civil & Environmental Engineering",
    "email": "erica.babusci@duke.edu",
    "location": "Durham, NC, 27705",
    "headshot": "/static/images/headshot.jpg",
    "profiles": {
        "linkedin": "https://www.linkedin.com/in/erica-babusci",
        "google_scholar": "https://scholar.google.com/citations?hl=en&user=exzOHD4AAAAJ&view_op=list_works&gmla=AF9nlQvI289VNmLvXHr3kJeiCoDVz-MemAIwwN3W4wKlTNLKj7eBNRSjNV1OBZz_7zckDzb57v_Vz9RXbVaOYWFA",
        "gunsch_lab": "https://gunsch.pratt.duke.edu/"
    },
    "cv_file": "/static/files/EMB_CV_2026.pdf",
    "intro": "Environmental microbiome engineering focused on microbial remediation and environmental mapping.",
# data.py (add inside site_data)
"news": [
    {
        "date": "FEB 20, 2026",
        "body": "Paper accepted to be published in ASM Microbiology Resource Announcements",
        "link": None   # <- replace with URL if you have one (e.g. 'https://...'), otherwise None
    }
],
    "projects": [
        {
            "id": "microencap",
            "title": "Microencapsulation of Microbes to Enhance Bioremediation of PAHs",
            "image": "/static/images/proj_microencap.png",
            "overview": "Research on microencapsulation strategies to improve survival and biodegradation of PAH-degrading microbes. Lab-based experiments, viability testing, and biodegradation assays.",
            "summary": (
                "Polycyclic aromatic hydrocarbons (PAHs) are persistent environmental contaminants "
                "composed of two or more fused benzene rings. Their chemical stability allows them to "
                "remain in soils and sediments for extended periods of time, and many PAHs are known "
                "to be carcinogenic or mutagenic, posing significant risks to human and ecosystem health.\n\n"
                "Bioremediation offers a cost-effective and sustainable strategy for addressing PAH "
                "contamination by harnessing microbial metabolism to degrade these compounds. However, "
                "in situ bioaugmentation efforts often produce inconsistent results because introduced "
                "microbes struggle to survive environmental stressors and compete with established native "
                "microbial communities.\n\n"
                "This project investigates microbial microencapsulation as a strategy to enhance the "
                "stability and reliability of bioaugmentation. Using ionic gelation, PAH-degrading "
                "microorganisms are encapsulated within a sodium alginate matrix to form stable, porous "
                "microcapsules. These capsules are designed to protect introduced organisms, buffer them "
                "against environmental stress, and allow for gradual release into the surrounding system. "
                "By improving microbial persistence and controlled delivery, this work advances a more "
                "predictable and scalable framework for environmental remediation."
            ),
            "collaborators": [
                {
                    "name": "Duke Superfund Research Center",
                    "url": "https://sites.nicholas.duke.edu/superfund/"
                }
            ],
            "publications": [
                {
                    "title": "Draft Genome Sequence of PAH-Degrading Fungal Isolates Trichoderma deliquescens and Aureobasidium sp.",
                    "venue": "Microbiology Resource Announcements",
                    "year": "2026 (Accepted)",
                    "url": "#"
                }
            ],
            "presentations": [
                {
                    "title": "Optimizing Fungal Microencapsulation for Bioremediation of PAHs",
                    "type": "Poster",
                    "venue": "FEMS Micro 2025, Milan, Italy",
                    "date": "July 2025",
                    "poster": "/static/files/FEMS_Poster_Copy (1).pptx",
                    "abstract": "/static/files/FEMS Micro 2025 Abstract (1).docx"
                },
                {
                    "title": "Microencapsulation as a Strategy for Precision Microbiome Engineering in Superfund Site Remediation",
                    "type": "Oral Presentation",
                    "venue": "Superfund Annual Meeting",
                    "date": "Dec 2025",
                    "poster": None,
                    "abstract": None
                }
            ]
        },
        {
            "id": "solar-panels",
            "title": "Metagenomic Analysis of Microbial Communities on Solar Panels",
            "image": "/static/images/proj_solar.jpg",
            "overview": "Metagenomic characterization of fungal biosoiling on photovoltaic panels and its relationship to land use, environmental conditions, and solar performance loss.",
            "summary": (
                "Solar panels are a critical component of renewable energy infrastructure, converting "
                "sunlight into electricity to power homes and communities. Over time, however, their "
                "efficiency declines due to soiling, which is the accumulation of material on panel surfaces "
                "that reduces light transmission.\n\n"
                "Soiling has traditionally been attributed to abiotic factors such as dust, pollen, "
                "and atmospheric particulates. However, large-scale imaging and field observations "
                "have revealed that fungal colonization plays a substantial role in performance losses. "
                "Biological fouling introduces a dynamic component to surface degradation, as fungi "
                "can adhere, grow, and persist under harsh environmental conditions.\n\n"
                "This project focuses on characterizing fungal communities colonizing solar panels "
                "using metagenomic sequencing approaches and linking community composition to land use "
                "and environmental context. By identifying ecological drivers of fungal colonization, "
                "this work aims to inform improved mitigation strategies and cleaning protocols that "
                "preserve photovoltaic performance and extend infrastructure longevity."
            ),
            "collaborators": [
                {
                    "name": "Solar Unsoiled",
                    "url": "https://www.solarunsoiled.com"
                },

            ],
            "publications": [
                {
                    "title": "Persistent Soiling: The Widespread Impact of Fungal Bio-Soiling to Photovoltaic Energy",
                    "venue": "In Preparation",
                    "year": "In Prep",
                    "url": "#"
                }
            ],
            "presentations": [
                {
                    "title": "Metagenomic Analysis of Microbial Genera on Solar Panels",
                    "type": "Poster",
                    "venue": "AEESP 2025 Research and Education Conference, Durham, NC",
                    "date": "May 2025",
                    "poster": "/static/files/AEESP_Poster_051325.pptx",
                    "abstract": "/static/files/EMB_AEESP_Abstract_2025_CKG.docx"
                }
            ]
        },
        {
            "id": "micro-blaze",
            "title": "Testing Microbial Containing Detergents to Degrade PAHs on Firefighter Suits",
            "image": "/static/images/proj_firefighter.jpg",
            "overview": "Testing detergents and microbial treatments (Micro-Blaze) for removing PAHs from firefighter personal protective equipment to reduce exposure risks.",
            "summary": (
                "Firefighter turnout gear provides critical thermal protection during fire response, "
                "but it can also accumulate hazardous chemicals such as polycyclic aromatic hydrocarbons (PAHs). "
                "These compounds are persistent, carcinogenic contaminants formed during combustion and "
                "have been linked to increased cancer risk among firefighters.\n\n"
                "This project evaluated the performance of a commercially marketed microbe-containing "
                "detergent (MCD) designed to degrade PAHs from contaminated textiles. Because the product "
                "is substantially more expensive than conventional detergents, its effectiveness was "
                "systematically assessed under varying washing conditions, including differences in "
                "agitation, detergent type, and wash duration.\n\n"
                "The study examined whether microbial degradation meaningfully enhanced chemical removal "
                "beyond what is achieved through conventional washing mechanisms. By comparing PAH removal "
                "efficiency across treatment conditions, this work aimed to determine whether biological "
                "additives provide measurable remediation benefits for contaminated protective gear.\n\n"
                "The findings contribute to evidence-based evaluation of emerging decontamination products "
                "and inform best practices for reducing firefighter occupational exposure."
            ),
            "publications": [
                {
                    "title": "Efficacy of Microbial Detergent in Degrading PAHs from Firefighter PPE",
                    "venue": "Journal of Occupational and Environmental Hygiene",
                    "year": "Under Review",
                    "url": "#"
                }
            ],
            "presentations": [
                {
                    "title": "Testing the Efficacy of Micro-Blaze Detergent on PAH Removal from Firefighter Uniforms",
                    "type": "Poster",
                    "venue": "International Fire Service Cancer Symposium 2025, ",
                    "date": "Feb 2025",
                    "poster": "/static/files/IFCS_25_Poster CKG.pptx",
                    "abstract": "/static/files/emb_IFCS25_abstract_CKG.docx"
                }
            ]
        },
        {
            "id": "Scensory",
            "title": "Automating Real-Time Fungal Identification and Spatial Mapping",
            "image": "/static/images/scensory.png",
            "overview": "Engineering alginate-based microencapsulation systems to improve survival, persistence, and biodegradation performance of PAH-degrading microbes in contaminated environments.",
            "summary": (
                "Indoor fungal growth can compromise air quality, building integrity, and human health, "
                "yet traditional identification methods rely on slow culturing techniques or manual sampling. "
                "This project developed Scensory, a robotic olfactory system capable of real-time fungal "
                "identification and spatial localization using low-cost volatile organic compound (VOC) sensors "
                "and deep learning models.\n\n"
                "The system integrates sensor arrays with automated robotic sampling to collect high-throughput "
                "VOC data from diverse fungal species. Neural network architectures were trained to classify "
                "species and infer their spatial origin from short temporal sensor signals, enabling rapid and "
                "accurate environmental assessment.\n\n"
                "This work demonstrates a scalable framework for autonomous fungal surveillance in built "
                "environments. By combining robotics, chemical sensing, and machine learning, the project "
                "advances real-time environmental monitoring and provides a foundation for early detection "
                "of harmful microbial contamination."
            ),
            "collaborators": [
                {
                    "name": "Duke Robotics Lab",
                    "url": "https://generalroboticslab.com"
                }
            ],
            "publications": [
                {
                    "title": "Scensory: Automated Real-Time Fungal Identification and Spatial Mapping",
                    "venue": "Nature Communications",
                    "year": "Under review",
                    "url": "https://www.researchgate.net/publication/395806353_Scensory_Automated_Real-Time_Fungal_Identification_and_Spatial_Mapping"
                }
            ],
            "presentations": [
                {
                    "title": "Rapid Fungal Typing and Spatial Mapping via VOC Sensing and Machine Learning",
                    "type": "Poster",
                    "venue": "PreMiEr Site Visit 2025",
                    "date": "June 2025",
                    "poster": "/static/files/scensory_post.pdf",
                    "abstract": None
                }
            ]
        },

    ],
    "publications": [
        {
            "title": "Draft Genome Sequence of PAH-Degrading Fungal Isolates Trichoderma deliquescens and Aureobasidium sp.",
            "venue": "Microbiology Resource Announcements",
            "year": "2026 (Accepted)",
            "url": "#"
        },
        {
            "title": "Isolation and characterization of 24 phages infecting Klebsiella sp. M5al",
            "venue": "PLOS One",
            "year": "2025",
            "url": "#"
        },
        {
            "title": "Efficacy of Microbial Detergent in Degrading PAHs from Firefighter PPE",
            "venue": "Journal of Occupational and Environmental Hygiene",
            "year": "Under Review",
            "url": "#"
        },
        {
            "title": "Persistent Soiling: The Widespread Impact of Fungal Bio-Soiling to Photovoltaic Energy",
            "venue": "In Preparation",
            "year": "In Prep",
            "url": "#"
        }
    ],

}
