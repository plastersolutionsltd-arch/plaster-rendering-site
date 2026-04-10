#!/usr/bin/env python3
"""Generate the 4 southeast Sheffield suburb pages from the southey template."""

import re

with open("southey-sheffield.html", "r") as f:
    TEMPLATE = f.read()

PAGES = [
    {
        "name": "Beighton",
        "postcode": "S20",
        "slug": "beighton-sheffield",
        "lat": "53.3540",
        "lng": "-1.3490",
        "hero_img": "greenhill-ewi.webp",
        "hero_alt": "EWI render completed in southeast Sheffield near Beighton S20 by P&R Solutions",
        "og_img_path": "case-studies/greenhill-ewi.webp",
        "meta_desc": "Plastering and rendering in Beighton Sheffield S20. Silicone render, monocouche, EWI and internal plastering across S20. 5★ rated. Free survey, no deposit.",
        "keywords": "plasterer Beighton Sheffield, renderer Beighton S20, silicone render Beighton, external wall insulation Beighton, EWI Beighton Sheffield, plastering Beighton, rendering S20 Sheffield",
        "geo_placename": "Beighton, Sheffield",
        "hero_label": "S20 · Sheffield, South Yorkshire",
        "hero_area": "Beighton.",
        "hero_para": "Beighton is a former mining village on the southeastern edge of Sheffield in the S20 postcode — a mix of traditional terraces, post-war semis and more recent housing estates. We cover S20 as part of our regular work across Sheffield.",
        "area_served": [
            '{"@type": "City", "name": "Sheffield"}',
            '{"@type": "AdministrativeArea", "name": "South Yorkshire"}',
            '{"@type": "Place", "name": "Beighton"}',
            '{"@type": "Place", "name": "Mosborough"}',
            '{"@type": "Place", "name": "Halfway"}',
            '{"@type": "Place", "name": "Crystal Peaks"}',
            '{"@type": "City", "name": "Rotherham"}',
            '{"@type": "City", "name": "Barnsley"}',
            '{"@type": "City", "name": "Doncaster"}',
        ],
        "faq": [
            {
                "num": "01", "cat": "Local",
                "q": "Do you cover Beighton and S20?",
                "a": "Yes — Beighton and the wider S20 postcode is within our working area. We cover southeast Sheffield regularly, travelling from our base in Grenoside S35. Free survey, no call-out charge."
            },
            {
                "num": "02", "cat": "Rendering",
                "q": "What render suits a Beighton property?",
                "a": "Beighton's mix of brick terraces and post-war semis respond well to silicone render — a clean, low-maintenance finish that seals ageing brickwork and requires no repainting. EWI with a silicone topcoat is also a popular choice for energy savings."
            },
            {
                "num": "03", "cat": "Insulation",
                "q": "Can you do EWI in Beighton?",
                "a": "Yes — many properties in Beighton are well-suited to EWI. We fit 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey available."
            },
            {
                "num": "04", "cat": "Plastering",
                "q": "Do you do internal plastering in Beighton?",
                "a": "Yes — full re-skims, dot and dab, stud partitions and ceiling boarding across S20. We cover the southeast of Sheffield and can often combine internal and external work on the same visit."
            },
            {
                "num": "05", "cat": "Pricing",
                "q": "How much does rendering cost in Beighton?",
                "a": "A typical Beighton semi starts from around £2,000–£3,500 for silicone or monocouche render, depending on size and access. We provide a free, itemised quote after a site visit so you know exactly what's included."
            },
        ],
        "services": {
            "silicone": "Beighton's brick terraces and post-war semis are ideal for silicone render — a clean, low-maintenance finish that seals and modernises older brickwork without repainting. A popular choice for southeast Sheffield homeowners looking to improve kerb appeal.",
            "monocouche": "For properties in Beighton where a more textured finish is preferred, monocouche scratch render is an excellent choice — through-colour, durable and built for the South Yorkshire climate. Colour-matched for a natural, consistent appearance.",
            "ewi": "EWI is a practical upgrade for Beighton's older housing stock — adding 90mm insulation boards with a silicone or monocouche topcoat. We back all EWI systems with a 25-year manufacturer warranty and offer free surveys.",
            "plastering": "Internal plastering across Beighton — full re-skims, ceiling repairs, new stud partitions and dot and dab boarding. We work efficiently across S20, minimising disruption and delivering a clean, flat finish.",
            "dry_lining": "Dot and dab plasterboard, metal stud partitions and ceiling boarding for Beighton homeowners — from room conversions to insulated dry lining on solid-wall properties. Clean, efficient and properly finished.",
        },
        "why_local": [
            "Beighton is a well-established area on the southeastern edge of Sheffield — the older brick terraces and post-war semis here are well suited to modern render and insulation upgrades.",
            "We cover S20 as part of our regular working area, travelling from Grenoside without fuss. Free survey, no call-out charge, and no deposit required before work begins.",
            "Silicone render and EWI have proved popular across southeast Sheffield as homeowners look to modernise and reduce energy bills. We're happy to advise at a free site visit.",
        ],
        "nearby_chips": [
            ("mosborough-sheffield", "Mosborough"),
            ("halfway-sheffield", "Halfway"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("woodseats-sheffield", "Woodseats"),
            ("norton-sheffield", "Norton"),
        ],
        "footer_chips": [
            ("mosborough-sheffield", "Mosborough"),
            ("halfway-sheffield", "Halfway"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("norton-sheffield", "Norton"),
            ("woodseats-sheffield", "Woodseats"),
            ("dore-sheffield", "Dore"),
        ],
    },
    {
        "name": "Mosborough",
        "postcode": "S20",
        "slug": "mosborough-sheffield",
        "lat": "53.3406",
        "lng": "-1.3649",
        "hero_img": "norton-silicone.webp",
        "hero_alt": "Silicone render completed in southeast Sheffield near Mosborough S20 by P&R Solutions",
        "og_img_path": "case-studies/norton-silicone.webp",
        "meta_desc": "Plastering and rendering in Mosborough Sheffield S20. Silicone render, monocouche, EWI and internal plastering across S20. 5★ rated. Free survey, no deposit.",
        "keywords": "plasterer Mosborough Sheffield, renderer Mosborough S20, silicone render Mosborough, external wall insulation Mosborough, EWI Mosborough Sheffield, plastering Mosborough, rendering S20 Sheffield",
        "geo_placename": "Mosborough, Sheffield",
        "hero_label": "S20 · Sheffield, South Yorkshire",
        "hero_area": "Mosborough.",
        "hero_para": "Mosborough is a residential area in southeast Sheffield with a village-like feel — a mix of 1970s and 80s housing and more recent development across the S20 postcode. We cover the area regularly as part of our south and southeast Sheffield work.",
        "area_served": [
            '{"@type": "City", "name": "Sheffield"}',
            '{"@type": "AdministrativeArea", "name": "South Yorkshire"}',
            '{"@type": "Place", "name": "Mosborough"}',
            '{"@type": "Place", "name": "Beighton"}',
            '{"@type": "Place", "name": "Halfway"}',
            '{"@type": "Place", "name": "Crystal Peaks"}',
            '{"@type": "City", "name": "Rotherham"}',
            '{"@type": "City", "name": "Barnsley"}',
            '{"@type": "City", "name": "Doncaster"}',
        ],
        "faq": [
            {
                "num": "01", "cat": "Local",
                "q": "Do you cover Mosborough and S20?",
                "a": "Yes — Mosborough and the surrounding S20 area is within our working area. We cover southeast Sheffield regularly and offer a free survey with no call-out charge."
            },
            {
                "num": "02", "cat": "Rendering",
                "q": "What render suits a Mosborough property?",
                "a": "Mosborough's 1970s and 80s housing stock is well suited to silicone render — a smooth, low-maintenance finish that seals ageing brick and requires no repainting. EWI with a silicone topcoat is also popular for homeowners wanting to improve energy efficiency."
            },
            {
                "num": "03", "cat": "Insulation",
                "q": "Can you do EWI in Mosborough?",
                "a": "Yes — many properties in Mosborough are excellent candidates for EWI. We install 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey to assess your property."
            },
            {
                "num": "04", "cat": "Plastering",
                "q": "Do you do internal plastering in Mosborough?",
                "a": "Yes — full re-skims, dot and dab, stud partitions and ceiling boarding across S20. We can often combine internal and external work in a single visit, saving time and disruption."
            },
            {
                "num": "05", "cat": "Pricing",
                "q": "How much does rendering cost in Mosborough?",
                "a": "A typical Mosborough semi starts from around £2,000–£3,500 for silicone or monocouche render, depending on size and access. We provide a free, itemised quote after a site visit."
            },
        ],
        "services": {
            "silicone": "Mosborough's 1970s and 80s housing is ideal for silicone render — a clean, smooth finish that seals older brickwork and keeps maintenance to a minimum. Popular with southeast Sheffield homeowners looking for a lasting upgrade without regular repainting.",
            "monocouche": "For Mosborough properties where a textured finish is preferred, monocouche scratch render is a great option — through-colour, durable and suited to the Sheffield climate. We colour-match to complement the local street scene.",
            "ewi": "EWI is an excellent fit for Mosborough's post-war and 70s housing stock. We fit 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey included.",
            "plastering": "Internal plastering in Mosborough — full re-skims, ceiling repairs, stud partitions and dot and dab boarding. We work across S20 regularly, keeping disruption to a minimum.",
            "dry_lining": "Dot and dab plasterboard, metal stud partitions and ceiling boarding for Mosborough homeowners — from room conversions to insulated dry lining on solid-wall properties.",
        },
        "why_local": [
            "Mosborough has a quieter, village-like feel compared to central Sheffield — but the housing stock, much of it from the 1970s and 80s, benefits greatly from modern render and insulation upgrades.",
            "We cover S20 as part of our regular southeast Sheffield work, travelling from Grenoside. Free survey, no call-out charge, no deposit required before we begin.",
            "Silicone render and EWI are both well suited to the cavity and solid-wall properties found across Mosborough. We're happy to advise on the right system at a free site visit.",
        ],
        "nearby_chips": [
            ("beighton-sheffield", "Beighton"),
            ("halfway-sheffield", "Halfway"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("woodseats-sheffield", "Woodseats"),
            ("norton-sheffield", "Norton"),
        ],
        "footer_chips": [
            ("beighton-sheffield", "Beighton"),
            ("halfway-sheffield", "Halfway"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("norton-sheffield", "Norton"),
            ("woodseats-sheffield", "Woodseats"),
            ("dore-sheffield", "Dore"),
        ],
    },
    {
        "name": "Halfway",
        "postcode": "S20",
        "slug": "halfway-sheffield",
        "lat": "53.3353",
        "lng": "-1.3759",
        "hero_img": "case/bentsgreen-ewi.webp",
        "hero_alt": "EWI rendering completed in southeast Sheffield near Halfway S20 by P&R Solutions",
        "og_img_path": "case-studies/case/bentsgreen-ewi.webp",
        "meta_desc": "Plastering and rendering in Halfway Sheffield S20. Silicone render, monocouche, EWI and internal plastering across S20. 5★ rated. Free survey, no deposit.",
        "keywords": "plasterer Halfway Sheffield, renderer Halfway S20, silicone render Halfway, external wall insulation Halfway, EWI Halfway Sheffield, plastering Halfway, rendering S20 Sheffield",
        "geo_placename": "Halfway, Sheffield",
        "hero_label": "S20 · Sheffield, South Yorkshire",
        "hero_area": "Halfway.",
        "hero_para": "Halfway is a large residential area in the south of Sheffield's S20 postcode — predominantly housing estates developed from the 1960s onwards, with a high proportion of properties suited to external render and insulation upgrades.",
        "area_served": [
            '{"@type": "City", "name": "Sheffield"}',
            '{"@type": "AdministrativeArea", "name": "South Yorkshire"}',
            '{"@type": "Place", "name": "Halfway"}',
            '{"@type": "Place", "name": "Mosborough"}',
            '{"@type": "Place", "name": "Beighton"}',
            '{"@type": "Place", "name": "Crystal Peaks"}',
            '{"@type": "City", "name": "Rotherham"}',
            '{"@type": "City", "name": "Barnsley"}',
            '{"@type": "City", "name": "Doncaster"}',
        ],
        "faq": [
            {
                "num": "01", "cat": "Local",
                "q": "Do you cover Halfway and S20?",
                "a": "Yes — Halfway and the surrounding S20 area is within our working area. We cover southeast Sheffield regularly, with a free survey and no call-out charge."
            },
            {
                "num": "02", "cat": "Rendering",
                "q": "What render suits a Halfway property?",
                "a": "Halfway's 1960s–80s housing estates include many properties ideal for silicone render — a clean, low-maintenance finish that modernises older brickwork and requires no repainting. EWI with a silicone topcoat is also popular for the energy savings."
            },
            {
                "num": "03", "cat": "Insulation",
                "q": "Can you do EWI in Halfway?",
                "a": "Yes — EWI is well suited to Halfway's estate housing. We install 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey available."
            },
            {
                "num": "04", "cat": "Plastering",
                "q": "Do you do internal plastering in Halfway?",
                "a": "Yes — full re-skims, dot and dab, stud partitions and ceiling boarding across S20. We're happy to combine internal and external work on the same job."
            },
            {
                "num": "05", "cat": "Pricing",
                "q": "How much does rendering cost in Halfway?",
                "a": "A typical Halfway semi starts from around £2,000–£3,500 for silicone or monocouche render, depending on size and access. We provide a free, itemised quote after a site visit."
            },
        ],
        "services": {
            "silicone": "Halfway's estate housing — much of it built in the 1960s and 70s — is well suited to silicone render. It seals ageing brickwork, modernises the property's appearance and requires no repainting. One of our most popular systems across southeast Sheffield.",
            "monocouche": "For Halfway homeowners wanting a textured finish, monocouche scratch render provides a through-colour, durable result built for the South Yorkshire climate. We colour-match to the local environment for a natural, consistent look.",
            "ewi": "EWI is a practical and cost-effective upgrade for Halfway's older housing stock — 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. We offer free surveys across S20.",
            "plastering": "Internal plastering across Halfway — full re-skims, ceiling repairs, new stud partitions and dot and dab boarding. We work efficiently across S20 with minimal disruption.",
            "dry_lining": "Dot and dab plasterboard, metal stud partitions and ceiling boarding for Halfway homeowners — from room conversions to full insulated dry lining. Properly finished and ready to decorate.",
        },
        "why_local": [
            "Halfway is one of the larger residential areas in southeast Sheffield — much of it developed from the 1960s onwards, with a housing stock that benefits well from modern render and insulation systems.",
            "We cover S20 regularly as part of our southeast Sheffield work, travelling from Grenoside. Free survey, no call-out charge, no deposit required before we start.",
            "EWI and silicone render are both popular in Halfway as homeowners upgrade their properties. We're happy to advise on the best system for your property at a free site visit.",
        ],
        "nearby_chips": [
            ("mosborough-sheffield", "Mosborough"),
            ("beighton-sheffield", "Beighton"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("woodseats-sheffield", "Woodseats"),
            ("norton-sheffield", "Norton"),
        ],
        "footer_chips": [
            ("mosborough-sheffield", "Mosborough"),
            ("beighton-sheffield", "Beighton"),
            ("crystal-peaks-sheffield", "Crystal Peaks"),
            ("gleadless-sheffield", "Gleadless"),
            ("norton-sheffield", "Norton"),
            ("woodseats-sheffield", "Woodseats"),
            ("dore-sheffield", "Dore"),
        ],
    },
    {
        "name": "Crystal Peaks",
        "postcode": "S20",
        "slug": "crystal-peaks-sheffield",
        "lat": "53.3520",
        "lng": "-1.3714",
        "hero_img": "s17-close-up-detail.webp",
        "hero_alt": "Render close-up finish on southeast Sheffield property near Crystal Peaks S20 by P&R Solutions",
        "og_img_path": "case-studies/s17-close-up-detail.webp",
        "meta_desc": "Plastering and rendering in Crystal Peaks Sheffield S20. Silicone render, monocouche, EWI and internal plastering across S20. 5★ rated. Free survey, no deposit.",
        "keywords": "plasterer Crystal Peaks Sheffield, renderer Crystal Peaks S20, silicone render Crystal Peaks, external wall insulation Crystal Peaks, EWI Crystal Peaks Sheffield, plastering Crystal Peaks, rendering S20 Sheffield",
        "geo_placename": "Crystal Peaks, Sheffield",
        "hero_label": "S20 · Sheffield, South Yorkshire",
        "hero_area": "Crystal Peaks.",
        "hero_para": "Crystal Peaks is a modern suburban area in southeast Sheffield, centred around the retail district of the same name. The surrounding S20 residential streets include a mix of post-war semis, 1970s–80s estates and newer builds — all well suited to external render and plastering work.",
        "area_served": [
            '{"@type": "City", "name": "Sheffield"}',
            '{"@type": "AdministrativeArea", "name": "South Yorkshire"}',
            '{"@type": "Place", "name": "Crystal Peaks"}',
            '{"@type": "Place", "name": "Beighton"}',
            '{"@type": "Place", "name": "Mosborough"}',
            '{"@type": "Place", "name": "Halfway"}',
            '{"@type": "City", "name": "Rotherham"}',
            '{"@type": "City", "name": "Barnsley"}',
            '{"@type": "City", "name": "Doncaster"}',
        ],
        "faq": [
            {
                "num": "01", "cat": "Local",
                "q": "Do you cover Crystal Peaks and S20?",
                "a": "Yes — the Crystal Peaks area and wider S20 postcode is within our regular working area. We cover southeast Sheffield and offer a free survey with no call-out charge."
            },
            {
                "num": "02", "cat": "Rendering",
                "q": "What render suits a Crystal Peaks property?",
                "a": "The mix of post-war and 1970s–80s properties around Crystal Peaks suits silicone render well — a clean, low-maintenance finish that seals brickwork and requires no repainting. EWI with a silicone topcoat is also popular for homeowners looking to improve energy efficiency."
            },
            {
                "num": "03", "cat": "Insulation",
                "q": "Can you do EWI near Crystal Peaks?",
                "a": "Yes — EWI works well on the estate housing surrounding Crystal Peaks. We install 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey available."
            },
            {
                "num": "04", "cat": "Plastering",
                "q": "Do you do internal plastering near Crystal Peaks?",
                "a": "Yes — full re-skims, dot and dab, stud partitions and ceiling boarding across S20. We can often combine internal and external work on the same visit."
            },
            {
                "num": "05", "cat": "Pricing",
                "q": "How much does rendering cost near Crystal Peaks?",
                "a": "A typical semi in the Crystal Peaks area starts from around £2,000–£3,500 for silicone or monocouche render, depending on size and access. We provide a free, itemised quote after a site visit."
            },
        ],
        "services": {
            "silicone": "The residential streets around Crystal Peaks include many post-war and 1970s brick properties ideal for silicone render — a smooth, clean finish that seals ageing brickwork and needs no repainting. A popular upgrade across southeast Sheffield.",
            "monocouche": "For Crystal Peaks area properties where a textured finish is preferred, monocouche scratch render provides a through-colour, durable result designed for the South Yorkshire climate. We colour-match for a natural, consistent look.",
            "ewi": "EWI is an effective upgrade for the post-war and 70s housing around Crystal Peaks. We install 90mm boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty and a free survey.",
            "plastering": "Internal plastering across the Crystal Peaks area — full re-skims, ceiling repairs, new stud partitions and dot and dab boarding. We work efficiently with minimal disruption across S20.",
            "dry_lining": "Dot and dab plasterboard, metal stud partitions and ceiling boarding for Crystal Peaks area homeowners — from room conversions to full insulated dry lining on solid-wall properties.",
        },
        "why_local": [
            "The Crystal Peaks area sits at the heart of southeast Sheffield's residential district — the surrounding streets include a range of property types from post-war semis to modern builds, many of which benefit from render and insulation upgrades.",
            "We cover S20 regularly from our base in Grenoside, with no call-out charge and no deposit required. Free survey available at a time that suits you.",
            "Silicone render and EWI are both popular choices in southeast Sheffield as homeowners look to improve energy performance and kerb appeal. We're happy to advise on the right system at a free visit.",
        ],
        "nearby_chips": [
            ("beighton-sheffield", "Beighton"),
            ("mosborough-sheffield", "Mosborough"),
            ("halfway-sheffield", "Halfway"),
            ("gleadless-sheffield", "Gleadless"),
            ("woodseats-sheffield", "Woodseats"),
            ("norton-sheffield", "Norton"),
        ],
        "footer_chips": [
            ("beighton-sheffield", "Beighton"),
            ("mosborough-sheffield", "Mosborough"),
            ("halfway-sheffield", "Halfway"),
            ("gleadless-sheffield", "Gleadless"),
            ("norton-sheffield", "Norton"),
            ("woodseats-sheffield", "Woodseats"),
            ("dore-sheffield", "Dore"),
        ],
    },
]


BIG_CHIP = '<a href="/{slug}" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">{label}</a>'
FOOTER_CHIP = '<a href="/{slug}" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">{label}</a>'
FOOTER_CHIP_SELF = '<span class="font-display text-[11px] px-2 py-0.5 rounded" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">{label}</span>'


def build_page(p):
    html = TEMPLATE

    name = p["name"]
    slug = p["slug"]
    pc = p["postcode"]
    lat = p["lat"]
    lng = p["lng"]
    hero_img = p["hero_img"]

    # --- Meta / head ---
    html = html.replace(
        "Plasterer &amp; Renderer in Southey Sheffield | P&amp;R Solutions",
        f"Plasterer &amp; Renderer in {name} Sheffield | P&amp;R Solutions"
    )
    html = html.replace(
        'content="Plastering and rendering in Southey Sheffield S5. Silicone render, monocouche, EWI and internal plastering across S5. 5★ rated. Free survey, no deposit."',
        f'content="{p["meta_desc"]}"'
    )
    html = html.replace(
        'content="plasterer Southey Sheffield, renderer Southey S5, silicone render Southey, external wall insulation Southey, EWI Southey Sheffield, plastering Southey, rendering S5 Sheffield"',
        f'content="{p["keywords"]}"'
    )
    html = html.replace(
        'content="Southey, Sheffield"',
        f'content="{p["geo_placename"]}"'
    )
    html = html.replace(
        'content="53.4254;-1.4602"',
        f'content="{lat};{lng}"'
    )
    html = html.replace(
        'content="53.4254, -1.4602"',
        f'content="{lat}, {lng}"'
    )
    html = html.replace(
        'href="https://www.plasterandrenderingsolutions.co.uk/southey-sheffield"',
        f'href="https://www.plasterandrenderingsolutions.co.uk/{slug}"'
    )

    # OG / Twitter
    html = html.replace(
        'content="https://www.plasterandrenderingsolutions.co.uk/southey-sheffield"',
        f'content="https://www.plasterandrenderingsolutions.co.uk/{slug}"'
    )
    html = html.replace(
        'content="Plastering and rendering in Southey S5. Silicone render, monocouche, EWI and plastering. Sheffield-based — free survey, zero deposit."',
        f'content="Plastering and rendering in {name} {pc}. Silicone render, monocouche, EWI and plastering. Sheffield-based — free survey, zero deposit."'
    )
    html = html.replace(
        'content="https://www.plasterandrenderingsolutions.co.uk/images/case-studies/shirecliffe-monocouche.webp"',
        f'content="https://www.plasterandrenderingsolutions.co.uk/images/{p["og_img_path"]}"'
    )
    html = html.replace(
        'content="Full plastering and rendering services in Southey Sheffield S5. Free survey, no deposit."',
        f'content="Full plastering and rendering services in {name} Sheffield {pc}. Free survey, no deposit."'
    )

    # --- Schema ---
    html = html.replace(
        '"latitude": "53.4254", "longitude": "-1.4602"',
        f'"latitude": "{lat}", "longitude": "{lng}"'
    )
    # areaServed
    area_served_json = ",\n          ".join(p["area_served"])
    html = re.sub(
        r'"areaServed": \[.*?\]',
        f'"areaServed": [\n          {area_served_json}\n        ]',
        html, flags=re.DOTALL
    )
    # WebPage schema
    html = html.replace(
        f'"@id": "https://www.plasterandrenderingsolutions.co.uk/southey-sheffield"',
        f'"@id": "https://www.plasterandrenderingsolutions.co.uk/{slug}"'
    )
    html = html.replace(
        f'"url": "https://www.plasterandrenderingsolutions.co.uk/southey-sheffield"',
        f'"url": "https://www.plasterandrenderingsolutions.co.uk/{slug}"'
    )
    html = html.replace(
        '"name": "Plasterer & Renderer in Southey Sheffield | P&R Solutions"',
        f'"name": "Plasterer & Renderer in {name} Sheffield | P&R Solutions"'
    )
    html = html.replace(
        '"description": "Plastering and rendering in Southey Sheffield S5 — silicone render, monocouche, EWI, internal plastering and dry lining. Free survey, zero deposit, 5-year guarantee."',
        f'"description": "Plastering and rendering in {name} Sheffield {pc} — silicone render, monocouche, EWI, internal plastering and dry lining. Free survey, zero deposit, 5-year guarantee."'
    )
    # FAQ schema
    faq_schema_items = []
    for fq in p["faq"]:
        faq_schema_items.append(
            f'{{"@type": "Question", "name": "{fq["q"]}", "acceptedAnswer": {{"@type": "Answer", "text": "{fq["a"]}"}}}}'
        )
    faq_schema = ",\n          ".join(faq_schema_items)
    html = re.sub(
        r'"mainEntity": \[.*?\]',
        f'"mainEntity": [\n          {faq_schema}\n        ]',
        html, flags=re.DOTALL
    )
    # Breadcrumb
    html = html.replace(
        '{"@type": "ListItem", "position": 3, "name": "Southey Sheffield", "item": "https://www.plasterandrenderingsolutions.co.uk/southey-sheffield"}',
        f'{{"@type": "ListItem", "position": 3, "name": "{name} Sheffield", "item": "https://www.plasterandrenderingsolutions.co.uk/{slug}"}}'
    )

    # --- Preload image ---
    html = html.replace(
        'href="/images/case-studies/shirecliffe-monocouche.webp"',
        f'href="/images/case-studies/{hero_img}"'
    )

    # --- Hero section ---
    html = html.replace(
        'src="/images/case-studies/shirecliffe-monocouche.webp"',
        f'src="/images/case-studies/{hero_img}"'
    )
    html = html.replace(
        'alt="Monocouche render completed in north Sheffield S5 by P&R Solutions"',
        f'alt="{p["hero_alt"]}"'
    )
    html = html.replace(
        '<span class="font-display text-xs font-bold tracking-[.35em] uppercase" style="color:#00FF00">S5 · Sheffield, South Yorkshire</span>',
        f'<span class="font-display text-xs font-bold tracking-[.35em] uppercase" style="color:#00FF00">{p["hero_label"]}</span>'
    )
    html = html.replace(
        '<h1 class="reveal delay-2 font-display font-light text-white/50 leading-[.92] tracking-tight" style="font-size:clamp(3.2rem,9vw,8rem)">Southey.</h1>',
        f'<h1 class="reveal delay-2 font-display font-light text-white/50 leading-[.92] tracking-tight" style="font-size:clamp(3.2rem,9vw,8rem)">{p["hero_area"]}</h1>'
    )
    html = html.replace(
        "Southey is a well-established residential area in north Sheffield in the S5 postcode — a mix of post-war semis, terraces and ex-council housing. We work regularly across S5, providing rendering and plastering services on all types of property.",
        p["hero_para"]
    )
    html = html.replace(
        '<span class="font-body text-white/60 text-sm"><span class="text-white font-semibold">98 Google reviews</span> &nbsp;·&nbsp; 5.0 stars</span>',
        '<span class="font-body text-white/60 text-sm"><span class="text-white font-semibold">98 Google reviews</span> &nbsp;·&nbsp; 5.0 stars</span>'
    )

    # --- Services section ---
    html = html.replace(
        'All Services in <span style="color:#37D413">Southey</span>',
        f'All Services in <span style="color:#37D413">{name}</span>'
    )
    html = html.replace(
        "Southey's post-war and ex-council brick properties are ideal for silicone render — a clean, low-maintenance finish that seals ageing brickwork, improves appearance and requires no repainting. One of our most popular finishes across north Sheffield.",
        p["services"]["silicone"]
    )
    html = html.replace(
        "For Southey properties where a more textured finish is preferred, monocouche scratch render is an excellent choice — through-colour, durable and well suited to the Sheffield climate. Colour-matched to the local area for a natural, consistent look.",
        p["services"]["monocouche"]
    )
    html = html.replace(
        "EWI is particularly popular in Southey — the area's post-war housing benefits significantly from added insulation, cutting heating bills and improving comfort. We fit 90mm boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty.",
        p["services"]["ewi"]
    )
    html = html.replace(
        "Internal plastering across Southey — full re-skims, ceiling repairs, new stud partitions and dot and dab boarding. We work efficiently across S5, minimising disruption and delivering a clean, flat finish ready for decoration.",
        p["services"]["plastering"]
    )
    html = html.replace(
        "Dot and dab plasterboard, metal stud partitions and ceiling boarding for Southey homeowners — from room conversions and divides to insulated dry lining on older solid-wall properties. Clean, efficient and properly finished.",
        p["services"]["dry_lining"]
    )

    # --- Why local ---
    html = html.replace(
        'Rendering &amp; Plastering in <span style="color:#37D413">Southey</span>',
        f'Rendering &amp; Plastering in <span style="color:#37D413">{name}</span>'
    )
    html = html.replace(
        "Southey is one of north Sheffield's established residential areas — the post-war housing stock here includes many solid brick semis and terraces that respond well to modern render and insulation upgrades.",
        p["why_local"][0]
    )
    html = html.replace(
        "We cover S5 as part of our regular working area and make the trip into Southey without fuss. Free survey, no call-out charge, and no deposit required before work begins.",
        p["why_local"][1]
    )
    html = html.replace(
        "Silicone render and EWI have both proved popular in Southey as homeowners look to modernise their properties and reduce energy bills. We're happy to advise at a free site visit.",
        p["why_local"][2]
    )

    # --- FAQ section ---
    html = html.replace(
        'Southey <span style="color:#37D413">FAQ</span>',
        f'{name} <span style="color:#37D413">FAQ</span>'
    )
    # Replace FAQ Q&A blocks
    faq_blocks_old = [
        ('Do you cover Southey and S5?', "Yes — Southey and the wider S5 postcode is within our regular working area. We're based in Grenoside, S35 and work across north Sheffield regularly. Free survey, no call-out charge."),
        ('What render suits a Southey semi?', "Southey's typical post-war and ex-council brick semis are ideal for silicone render — a clean, low-maintenance finish that modernises the look and requires no repainting. EWI with a silicone topcoat is also popular for the added energy savings."),
        ('Can you do EWI in Southey?', "Yes — EWI is a great fit for Southey's post-war housing stock. We fit 90mm insulation boards with a silicone or monocouche topcoat, backed by a 25-year manufacturer warranty. Free survey to assess your property."),
        ('Do you do internal plastering in Southey?', "Yes — full re-skims, dot and dab, stud partitions and ceiling boarding across S5. We often combine internal and external work on the same visit, saving time and disruption."),
        ('How much does rendering cost in Southey?', "A typical Southey semi starts from around £2,000–£3,500 for silicone or monocouche render, depending on size and access. We provide a free, itemised quote after a site visit so you know exactly what's included."),
    ]
    for i, (old_q, old_a) in enumerate(faq_blocks_old):
        new_faq = p["faq"][i]
        html = html.replace(f'<div class="faq-q">{old_q}</div>', f'<div class="faq-q">{new_faq["q"]}</div>')
        html = html.replace(f'<p class="faq-ans">{old_a}</p>', f'<p class="faq-ans">{new_faq["a"]}</p>')
        html = html.replace(f'<span class="faq-cat">{["Local","Rendering","Insulation","Plastering","Pricing"][i]}</span>',
                            f'<span class="faq-cat">{new_faq["cat"]}</span>', 1)

    # --- CTA ---
    html = html.replace(
        'Get a Free Survey<br><span style="color:#37D413">in Southey</span>',
        f'Get a Free Survey<br><span style="color:#37D413">in {name}</span>'
    )
    html = html.replace(
        f'No deposit required. We survey, quote and — when you are ready — deliver a finish you will be proud of. Call us or fill in the form and we will be in touch within 24 hours.',
        f'No deposit required. We survey, quote and — when you are ready — deliver a finish you will be proud of. Call us or fill in the form and we will be in touch within 24 hours.'
    )

    # --- Nearby chips (big) ---
    old_chips_block = (
        '<a href="/firth-park-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Firth Park</a>\n'
        '      <a href="/chapeltown-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Chapeltown</a>\n'
        '      <a href="/ecclesfield-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Ecclesfield</a>\n'
        '      <a href="/high-green-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">High Green</a>\n'
        '      <a href="/hillsborough-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Hillsborough</a>\n'
        '      <a href="/malin-bridge-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Malin Bridge</a>\n'
        '      <a href="/wisewood-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Wisewood</a>\n'
        '            <a href="/parson-cross-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Parson Cross</a>\n'
        '            <a href="/wincobank-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Wincobank</a>\n'
        '      <a href="/silicone-render-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Silicone Rendering Sheffield</a>\n'
        '      <a href="/ewi-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">EWI Sheffield</a>\n'
        '      <a href="/plastering-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Plastering Sheffield</a>\n'
        '      <a href="/monocouche-render-sheffield" class="font-display text-sm font-semibold no-underline px-5 py-2.5 rounded-full transition-all duration-200" style="background:#131313;border:1px solid #1e1e1e;color:rgba(255,255,255,0.65)" onmouseover="this.style.borderColor=\'#00FF00\';this.style.color=\'#00FF00\'" onmouseout="this.style.borderColor=\'#1e1e1e\';this.style.color=\'rgba(255,255,255,0.65)\'">Monocouche Sheffield</a>'
    )
    new_area_chips = "\n      ".join([
        BIG_CHIP.format(slug=s, label=l) for s, l in p["nearby_chips"]
    ])
    new_area_chips += "\n      " + BIG_CHIP.format(slug="silicone-render-sheffield", label="Silicone Rendering Sheffield")
    new_area_chips += "\n      " + BIG_CHIP.format(slug="ewi-sheffield", label="EWI Sheffield")
    new_area_chips += "\n      " + BIG_CHIP.format(slug="plastering-sheffield", label="Plastering Sheffield")
    new_area_chips += "\n      " + BIG_CHIP.format(slug="monocouche-render-sheffield", label="Monocouche Sheffield")
    html = html.replace(old_chips_block, new_area_chips)

    # --- Footer chips ---
    # Replace the footer chips block for southey's self-link + area links
    old_footer_chips = (
        '<a href="/southey-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Southey</a>\n'
        '          <a href="/firth-park-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Firth Park</a>\n'
        '          <a href="/chapeltown-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Chapeltown</a>\n'
        '          <a href="/hillsborough-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Hillsborough</a>\n'
        '          <a href="/grenoside-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Grenoside</a>\n'
        '          <a href="/walkley-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Walkley</a>\n'
        '          <a href="/malin-bridge-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Malin Bridge</a>\n'
        '          <a href="/wisewood-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Wisewood</a>\n'
        '          <a href="/stannington-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Stannington</a>\n'
        '          <a href="/dore-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Dore</a>\n'
        '          <a href="/totley-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Totley</a>\n'
        '          <a href="/norton-sheffield" class="font-display text-[11px] px-2 py-0.5 rounded no-underline" style="color:rgba(255,255,255,0.45);background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08)">Norton</a>'
    )
    new_footer_chips_list = []
    # self-link as span
    new_footer_chips_list.append(FOOTER_CHIP_SELF.format(label=name))
    for s, l in p["footer_chips"]:
        new_footer_chips_list.append(FOOTER_CHIP.format(slug=s, label=l))
    new_footer_chips = "\n          ".join(new_footer_chips_list)
    html = html.replace(old_footer_chips, new_footer_chips)

    return html


for page in PAGES:
    html = build_page(page)
    fname = f"{page['slug']}.html"
    with open(fname, "w") as f:
        f.write(html)
    print(f"Generated {fname}")

print("Done.")
