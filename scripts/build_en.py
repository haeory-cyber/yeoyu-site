#!/usr/bin/env python3
"""Build yeoyu/en/index.html from yeoyu/index.html by exact-string replacement.
Every replacement must match exactly the expected number of times, else abort."""
import re, sys, pathlib

ROOT = pathlib.Path('/home/haeory/poomasi/yeoyu')
src = (ROOT / 'index.html').read_text(encoding='utf-8')
out = src

R = []  # (old, new, expected_count)
def rep(old, new, n=1): R.append((old, new, n))

# ---------- HEAD ----------
rep('<html lang="ko">', '<html lang="en">')
rep('<title>여유로와 | 충남 논산 프라이빗 독채 풀빌라</title>',
    '<title>Yeoyurowa | Private Countryside Villa with Jacuzzi in Nonsan, Korea</title>')
rep('<meta name="description" content="충청남도 논산 가야곡면의 프라이빗 독채 풀빌라. 자연 속 완전한 여유를 경험하세요. 바비큐, 수영장, 스파 완비. 커플·가족 여행 추천.">',
    '<meta name="description" content="A private whole-house villa in the quiet countryside of Nonsan, Chungcheongnam-do, Korea. Jacuzzi, garden BBQ, fire pit and three bedrooms for up to 10 guests. Ideal for couples, families and small groups.">')
rep('<meta name="keywords" content="논산 풀빌라, 논산 독채펜션, 충남 풀빌라, 논산 커플펜션, 논산 가족펜션, 가야곡 펜션, 여유로와">',
    '<meta name="keywords" content="Nonsan villa, Korea countryside stay, private house rental Korea, Nonsan pension, jacuzzi villa Korea, Chungcheongnam-do accommodation, Yeoyurowa">')
rep('<link rel="canonical" href="https://yeoyu.co.kr/">', '<link rel="canonical" href="https://yeoyu.co.kr/en/">')
rep('<meta property="og:title" content="여유로와 | 충남 논산 프라이빗 독채 풀빌라">',
    '<meta property="og:title" content="Yeoyurowa | Private Countryside Villa with Jacuzzi in Nonsan, Korea">')
rep('<meta property="og:description" content="충청남도 논산 가야곡면의 프라이빗 독채 풀빌라. 자연 속 완전한 여유를 경험하세요.">',
    '<meta property="og:description" content="A private whole-house villa in the countryside of Nonsan, Korea. Jacuzzi, garden BBQ and unhurried days for up to 10 guests.">')
rep('<meta property="og:url" content="https://yeoyu.co.kr/">', '<meta property="og:url" content="https://yeoyu.co.kr/en/">')
rep('<meta property="og:locale" content="ko_KR">', '<meta property="og:locale" content="en_US">\n  <meta property="og:locale:alternate" content="ko_KR">')
rep('<meta property="og:site_name" content="여유로와">', '<meta property="og:site_name" content="Yeoyurowa">')
# JSON-LD
rep('  "name": "여유로와",\n  "description": "충청남도 논산 가야곡면의 프라이빗 독채 풀빌라. 바비큐, 수영장, 스파 완비.",\n  "url": "https://yeoyu.co.kr",',
    '  "name": "Yeoyurowa",\n  "alternateName": "여유로와",\n  "inLanguage": "en",\n  "description": "A private whole-house villa in the countryside of Nonsan, Chungcheongnam-do, Korea. Jacuzzi, garden BBQ, fire pit, three bedrooms, up to 10 guests.",\n  "url": "https://yeoyu.co.kr/en/",\n  "telephone": "+82-10-4342-9712",\n  "checkinTime": "15:00",\n  "checkoutTime": "11:00",')
rep('"streetAddress": "가야곡면 강청길 32"', '"streetAddress": "32 Gangcheong-gil, Gayagok-myeon"')
rep('"addressLocality": "논산시"', '"addressLocality": "Nonsan-si"')
rep('"addressRegion": "충청남도"', '"addressRegion": "Chungcheongnam-do"')
rep('{"@type": "LocationFeatureSpecification", "name": "수영장", "value": true},', '{"@type": "LocationFeatureSpecification", "name": "Jacuzzi", "value": true},')
rep('{"@type": "LocationFeatureSpecification", "name": "바비큐", "value": true},', '{"@type": "LocationFeatureSpecification", "name": "Garden BBQ", "value": true},')
rep('{"@type": "LocationFeatureSpecification", "name": "스파", "value": true},', '{"@type": "LocationFeatureSpecification", "name": "Fire pit", "value": true},')
rep('{"@type": "LocationFeatureSpecification", "name": "독채", "value": true}', '{"@type": "LocationFeatureSpecification", "name": "Entire house", "value": true}')

# ---------- NAV / HERO ----------
rep('<a href="#main" class="skip-link">본문으로 바로가기</a>', '<a href="#main" class="skip-link">Skip to main content</a>')
rep('aria-label="주 내비게이션"', 'aria-label="Main navigation"')
rep('aria-label="여유로와 홈"', 'aria-label="Yeoyurowa home"')
rep('<img src="images/logo.png" alt="여유로와" width="170" height="120">', '<img src="/images/logo.png" alt="Yeoyurowa" width="170" height="120">')
rep('<a href="#exterior" class="nav__link" data-spy="exterior">공간</a>', '<a href="#exterior" class="nav__link" data-spy="exterior">Spaces</a>')
rep('<a href="#amenities" class="nav__link" data-spy="amenities">시설</a>', '<a href="#amenities" class="nav__link" data-spy="amenities">Facilities</a>')
rep('<a href="#gallery" class="nav__link" data-spy="gallery">갤러리</a>', '<a href="#gallery" class="nav__link" data-spy="gallery">Gallery</a>')
rep('<a href="#pricing" class="nav__link" data-spy="pricing">요금</a>', '<a href="#pricing" class="nav__link" data-spy="pricing">Rates</a>')
rep('<a href="#availability" class="nav__link" data-spy="availability">예약</a>', '<a href="#availability" class="nav__link" data-spy="availability">Book</a>')
rep('<a href="#eats" class="nav__link" data-spy="eats">주변 맛집</a>', '<a href="#eats" class="nav__link" data-spy="eats">Eat Nearby</a>')
rep('<a href="#info" class="nav__link" data-spy="info">안내</a>', '<a href="#info" class="nav__link" data-spy="info">Info</a>')
rep('<a href="/en/" class="nav__lang" lang="en" hreflang="en">EN</a>', '<a href="/" class="nav__lang" lang="ko" hreflang="ko" aria-label="Korean version">\ud55c\uad6d\uc5b4</a>')
rep('<a href="#availability" class="nav__cta">예약하기</a>', '<a href="#availability" class="nav__cta">Book</a>')
rep('<span class="hero__label reveal">충남 논산 · 프라이빗 독채</span>', '<span class="hero__label reveal">Nonsan, Korea · Private whole house</span>')
rep('aria-label="메인 헤더"', 'aria-label="Main header"')
rep('src="images/hero.jpg" alt="" aria-hidden="true" loading="eager"', 'src="/images/hero.jpg" alt="" aria-hidden="true" loading="eager"')
rep('          여유로운 이곳으로<br><em>여유로와</em>', '          Come to where<br><em>time slows down</em>')
rep('          좋은 사람들과, 아무 걱정 없는 하루.', '          Yeoyurowa — a private countryside house in Nonsan, Korea.<br>Good company, and a day with nothing to worry about.')
rep('<a href="#availability" class="btn-primary">예약하기</a>', '<a href="#availability" class="btn-primary">Book a stay</a>')
rep('<a href="#exterior" class="btn-ghost">공간 살펴보기</a>', '<a href="#exterior" class="btn-ghost">Explore the house</a>')

# ---------- EXTERIOR ----------
rep('<img src="images/hero.jpg" alt="여유로와 외관" loading="lazy" id="exteriorImg">', '<img src="/images/hero.jpg" alt="Exterior of Yeoyurowa" loading="lazy" id="exteriorImg">')
rep('          느긋하게<br><em>머물다 가는 곳</em>', '          A place to<br><em>linger a while</em>')
rep('          논산 탑정호 인근, 한적한 시골마을에 자리한 공유별장. 넓은 마당과 계절마다 다른 풍경이 어우러져 머무는 것 자체가 힐링입니다.',
    '          A shared country house in a quiet village near Tapjeong Lake, Nonsan. With a wide garden and scenery that changes with the seasons, simply being here is the rest you came for.')

# ---------- INTERIOR ----------
rep('            천천히 스며드는<br><em>편안함</em>', '            Comfort that<br><em>settles in slowly</em>')
rep('            따뜻한 실내 공간, 호텔식 순면 침구. 바쁜 일상에서 잠시 벗어나 여유로운 시간을 보낼 수 있도록 준비했습니다.',
    '            Warm interiors and hotel-grade cotton bedding. Everything is prepared so you can step away from a busy life and take your time.')
rep('<img src="images/interior-living.jpg" alt="여유로와 거실" loading="lazy">', '<img src="/images/interior-living.jpg" alt="Living room at Yeoyurowa" loading="lazy">')
rep('<img src="images/interior-loft.jpg" alt="여유로와 다락방" loading="lazy">', '<img src="/images/interior-loft.jpg" alt="Loft at Yeoyurowa" loading="lazy">')

# ---------- OFFERS ----------
rep('              아무것도 하지 않아도<br><em>좋은 하루</em>', '              A good day,<br><em>even doing nothing</em>')
rep('            바베큐 연기가 피어오르는 저녁, 자쿠지에서 보내는 밤, 마당에서 마시는 아침 커피 한 잔. 조용히 쉬고 싶은 날, 여유로와에서.',
    '            An evening of BBQ smoke drifting up, a night in the jacuzzi, a morning coffee in the garden. For the days you simply want quiet, come to Yeoyurowa.')
rep('<h3 class="offer-card__title">자쿠지</h3>', '<h3 class="offer-card__title">Jacuzzi</h3>')
rep('추가 비용 없이 프라이빗하게 즐기는 자쿠지. 천천히 물을 채우는 시간(약 2시간)마저 여유로운 쉼의 일부가 됩니다.',
    'A private jacuzzi at no extra cost. Even the slow filling of the tub (about two hours) becomes part of the unhurried rest.')
rep('<h3 class="offer-card__title">마당 바베큐</h3>', '<h3 class="offer-card__title">Garden BBQ</h3>')
rep('야외 정자와 화로대가 준비된 넓은 마당. 밤하늘 아래서 따뜻한 불멍과 맛있는 바베큐를 마음껏 즐겨보세요.',
    'A wide garden with an outdoor pavilion and fire pit. Enjoy a warm fire and a good BBQ under the night sky.')
rep('<h3 class="offer-card__title">거실 라운지</h3>', '<h3 class="offer-card__title">Living Lounge</h3>')
rep('TV가 없는 거실은 오직 좋은 음악과 서로의 목소리로만 채워집니다. 일상에서 미뤄두었던 서로의 이야기에 귀 기울이며 우리만의 여유로운 시간을 가져보세요.',
    'There is no TV in the living room. It is filled only with good music and each other\'s voices. Catch up on the conversations everyday life kept postponing.')
rep('<h3 class="offer-card__title">키친 &amp; 다이닝</h3>', '<h3 class="offer-card__title">Kitchen &amp; Dining</h3>')
rep('정성껏 준비한 식기와 조리도구가 완비된 주방입니다. 맛있는 음식을 함께 만들고 마주 앉아 소중한 이야기를 나누는 시간을 즐겨보세요.',
    'A fully equipped kitchen with carefully chosen tableware and cookware. Cook together, sit across from each other, and share the stories that matter.')

# ---------- AMENITIES ----------
rep('<h2 class="section-heading reveal reveal-delay-1" id="amenities-title">시설 <em>안내</em></h2>', '<h2 class="section-heading reveal reveal-delay-1" id="amenities-title">Facilities &amp; <em>Amenities</em></h2>')
rep('<div class="amenity-name">독채 전용</div><div class="amenity-sub">6인 기준, 최대 10인</div>', '<div class="amenity-name">Entire house</div><div class="amenity-sub">Base 6 guests, up to 10</div>')
rep('<div class="amenity-name">넓은 야외 마당</div><div class="amenity-sub">캠핑 가능</div>', '<div class="amenity-name">Large garden</div><div class="amenity-sub">Camping allowed</div>')
rep('<div class="amenity-name">야외 바베큐장</div><div class="amenity-sub">그릴 무료, 숯 3만원</div>', '<div class="amenity-name">Outdoor BBQ area</div><div class="amenity-sub">Grill free, charcoal set ₩30,000</div>')
rep('<div class="amenity-name">자쿠지</div><div class="amenity-sub">무료 · 셀프 급수 (약 2시간)</div>', '<div class="amenity-name">Jacuzzi</div><div class="amenity-sub">Free · self-fill (about 2 hours)</div>')
rep('<div class="amenity-name">불멍 화롯대</div><div class="amenity-sub">무료, 장작 1.5만원</div>', '<div class="amenity-name">Fire pit</div><div class="amenity-sub">Free, firewood ₩15,000</div>')
rep('<div class="amenity-name">개별욕실</div><div class="amenity-sub">독립욕실 2개</div>', '<div class="amenity-name">Bathrooms</div><div class="amenity-sub">2 separate bathrooms</div>')
rep('<div class="amenity-name">침실 3개</div><div class="amenity-sub">더블베드 3</div>', '<div class="amenity-name">3 bedrooms</div><div class="amenity-sub">3 double beds</div>')
rep('<div class="amenity-name">주방시설</div><div class="amenity-sub">인덕션, 식기완비</div>', '<div class="amenity-name">Kitchen</div><div class="amenity-sub">Induction cooktop, full tableware</div>')

# ---------- GALLERY ----------
rep('<h2 class="section-heading" id="gallery-title">공간 둘러보기</h2>', '<h2 class="section-heading" id="gallery-title">Look Around</h2>')

# ---------- PRICING ----------
rep('<h2 class="section-heading reveal reveal-delay-1" id="pricing-title">이용 요금 안내</h2>', '<h2 class="section-heading reveal reveal-delay-1" id="pricing-title">Rates</h2>')
rep('              온전한 휴식을 위한 프라이빗 독채 풀빌라입니다.<br>커플부터 가족 모임까지, 기본 6인부터 최대 10인까지 머무르실 수 있으며 기준 인원 초과 시 1인당 2만 원이 추가됩니다.<br>바베큐는 그릴과 숯 세팅을 요청하시거나, 직접 준비하고 세척해 주시는 조건으로 장비를 무료로 이용하실 수 있습니다.',
    '              The whole house is yours — a private villa with jacuzzi for a complete rest.<br>From couples to family gatherings, the base rate covers 6 guests and the house sleeps up to 10. Each additional guest is ₩20,000 per night.<br>For BBQ, ask us to set up the grill and charcoal, or bring your own supplies and use the equipment free of charge, provided you clean it afterwards.<br>All prices are in Korean won (KRW), per night.')
rep('<tr><th>구분</th><th>요금</th></tr>', '<tr><th>Item</th><th>Rate</th></tr>')
rep('<td>주말<small>금·토·공휴일 전날</small></td>\n                  <td>350,000원</td>', '<td>Weekend<small>Fri, Sat &amp; the night before public holidays</small></td>\n                  <td>₩350,000</td>')
rep('<td>평일</td>\n                  <td>250,000원</td>', '<td>Weekday</td>\n                  <td>₩250,000</td>')
rep('<td>추가 인원<small>1인당</small></td>\n                  <td>+20,000원</td>', '<td>Additional guest<small>per person</small></td>\n                  <td>+₩20,000</td>')
rep('<td>바베큐 — 그릴 및 숯 세팅</td>\n                  <td>+30,000원</td>', '<td>BBQ — grill &amp; charcoal set-up</td>\n                  <td>+₩30,000</td>')
rep('<td>바베큐 — 셀프 이용<small>세척 조건</small></td>\n                  <td>무료</td>', '<td>BBQ — self-service<small>clean-up required</small></td>\n                  <td>Free</td>')
rep('<td>장작</td>\n                  <td>+15,000원</td>', '<td>Firewood</td>\n                  <td>+₩15,000</td>')
rep('<p class="price-account">입금 계좌<br>카카오뱅크 3333-07-1187888 (예금주: 김성훈(여유로와))</p>',
    '<p class="price-account">Payment by bank transfer<br>KakaoBank 3333-07-1187888 (account holder: 김성훈(여유로와) / Kim Seong-hoon)<br>Paying from overseas? Contact us and we will arrange it together.</p>')

# ---------- AVAILABILITY ----------
rep('<h2 class="section-heading reveal reveal-delay-1" id="availability-title">실시간 <em>예약</em></h2>', '<h2 class="section-heading reveal reveal-delay-1" id="availability-title">Live <em>Availability</em></h2>')
rep('<p class="section-body reveal reveal-delay-2">예약현황 확인 후 예약하기를 이용해주세요.</p>',
    '<p class="section-body reveal reveal-delay-2">Check the calendar for open dates, then book. The booking calendar is provided by our Korean booking partner and is displayed in Korean. If you would rather book in English, call or text us at <a href="tel:+821043429712" style="color:var(--forest);text-decoration:underline;">+82 10-4342-9712</a> and we will reserve the dates for you.</p>')
rep('title="여유로와 예약 캘린더"', 'title="Yeoyurowa booking calendar"')
rep('aria-label="예약 페이지 새 탭으로 열기"', 'aria-label="Open the booking page in a new tab"')
rep('          캘린더가 보이지 않으면 <a href="https://booking.pension.onda.me/139407/calendar" target="_blank" rel="noopener" style="color:var(--forest);text-decoration:underline;">여기</a>를 눌러 새 창에서 여세요.',
    '          If the calendar does not load, <a href="https://booking.pension.onda.me/139407/calendar" target="_blank" rel="noopener" style="color:var(--forest);text-decoration:underline;">open it in a new window</a>.')

# ---------- INFO ----------
rep('<section class="info" id="info" aria-label="안내사항">', '<section class="info" id="info" aria-label="Guest information">')
rep('<h2 class="section-heading reveal reveal-delay-1" style="margin-bottom:36px;">안내사항</h2>', '<h2 class="section-heading reveal reveal-delay-1" style="margin-bottom:36px;">Good to Know</h2>')
rep('data-tab="tab-location" role="tab" aria-selected="true">위치안내</button>', 'data-tab="tab-location" role="tab" aria-selected="true">Location</button>')
rep('data-tab="tab-rules" role="tab" aria-selected="false">이용안내</button>', 'data-tab="tab-rules" role="tab" aria-selected="false">House Rules</button>')
rep('data-tab="tab-refund" role="tab" aria-selected="false">환불규정</button>', 'data-tab="tab-refund" role="tab" aria-selected="false">Cancellation</button>')
rep('src="https://maps.google.com/maps?q=충청남도+논산시+가야곡면+강청길+32&output=embed&hl=ko"', 'src="https://maps.google.com/maps?q=32+Gangcheong-gil,+Gayagok-myeon,+Nonsan-si,+Chungcheongnam-do,+South+Korea&output=embed&hl=en"')
rep('title="여유로와 위치 지도"', 'title="Map of Yeoyurowa"')
rep('<a href="https://map.kakao.com/link/search/충청남도 논산시 가야곡면 강청길 32"\n                target="_blank" rel="noopener noreferrer" class="map-link">카카오맵에서 보기 →</a>',
    '<a href="https://www.google.com/maps/search/?api=1&query=32+Gangcheong-gil,+Gayagok-myeon,+Nonsan-si,+Chungcheongnam-do,+South+Korea"\n                target="_blank" rel="noopener noreferrer" class="map-link">Open in Google Maps →</a>')
rep('<div class="loc-row"><dt>주소</dt><dd>충청남도 논산시 가야곡면 강청길 32</dd></div>',
    '<div class="loc-row"><dt>Address</dt><dd>32 Gangcheong-gil, Gayagok-myeon, Nonsan-si, Chungcheongnam-do, South Korea<br><span lang="ko">충청남도 논산시 가야곡면 강청길 32</span></dd></div>')
rep('<div class="loc-row"><dt>전화</dt><dd>010-4342-9712</dd></div>', '<div class="loc-row"><dt>Phone</dt><dd><a href="tel:+821043429712">+82 10-4342-9712</a></dd></div>')
rep('<div class="loc-row"><dt>주차</dt><dd>마당 내 최대 3대 주차 가능</dd></div>', '<div class="loc-row"><dt>Parking</dt><dd>Up to 3 cars in the garden</dd></div>')
rep('<div class="loc-row"><dt>주변관광</dt><dd>탑정호<br>탑정호 수변생태공원<br>딸기향 농촌테마공원<br>계백장군유적지 &amp; 백제군사박물관<br>논산 선샤인랜드</dd></div>',
    '<div class="loc-row"><dt>Nearby</dt><dd>Tapjeong Lake<br>Tapjeong Lake Waterside Eco Park<br>Strawberry Rural Theme Park<br>General Gyebaek Historic Site &amp; Baekje Military Museum<br>Nonsan Sunshine Land</dd></div>')
rep('<li><strong>체크인</strong> 15:00 / <strong>체크아웃</strong> 11:00</li>', '<li><strong>Check-in</strong> 3:00 pm / <strong>Check-out</strong> 11:00 am</li>')
rep('<li>다음 분을 위해 퇴실 시 가벼운 정리 정돈(분리수거, 식기 세척)을 부탁드립니다.</li>', '<li>Before you leave, please tidy up lightly for the next guests: sort the recycling and wash the dishes.</li>')
rep('<li>머무시는 분들의 쾌적한 환경을 위해 실내에서는 흡연을 삼가주세요.</li>', '<li>No smoking indoors, to keep the house fresh for everyone who stays here.</li>')
rep('<li>모두의 편안한 휴식을 위해 반려동물과의 동반 숙박은 어렵습니다.</li>', '<li>Pets cannot be accommodated, for the comfort of all guests.</li>')
rep('<li>보호자를 동반하지 않은 미성년자의 예약 및 입실은 제한됩니다.</li>', '<li>Minors cannot book or check in without a guardian.</li>')
rep('<li>온전한 쉼을 위해 예약된 인원 외 방문객의 출입을 엄격히 제한합니다.</li>', '<li>Only registered guests may enter the property. Visitors who are not part of the booking are strictly not allowed.</li>')
rep('<li>조용한 별장의 밤을 위해 22시 이후 바베큐 및 불멍 이용은 자제해 주세요.</li>', '<li>Please finish BBQ and fire-pit use by 10:00 pm so the village stays quiet at night.</li>')
rep('<li>정성껏 준비한 시설과 비품 훼손 시 부득이하게 변상비가 청구될 수 있습니다.</li>', '<li>Damage to the house, facilities or furnishings may be charged at cost.</li>')
rep('<thead><tr><th>취소 시점</th><th>환불 금액</th></tr></thead>', '<thead><tr><th>Cancelled</th><th>Refund</th></tr></thead>')
rep('<tr><td>이용 14일 전</td><td>100% 환불</td></tr>', '<tr><td>14 days or more before check-in</td><td>100% refund</td></tr>')
rep('<tr><td>이용 7일 전</td><td>70% 환불</td></tr>', '<tr><td>7 days before check-in</td><td>70% refund</td></tr>')
rep('<tr><td>이용 3일 전</td><td>50% 환불</td></tr>', '<tr><td>3 days before check-in</td><td>50% refund</td></tr>')
rep('<tr><td>이용 1일 전</td><td>30% 환불</td></tr>', '<tr><td>1 day before check-in</td><td>30% refund</td></tr>')
rep('<tr><td>당일 취소</td><td class="refund-none">환불 불가</td></tr>', '<tr><td>On the day of check-in</td><td class="refund-none">No refund</td></tr>')

# ---------- FOOTER ----------
rep('<img src="images/logo.png" alt="여유로와">', '<img src="/images/logo.png" alt="Yeoyurowa">')
rep('          상호: 여유로와 &nbsp;·&nbsp; 사업자등록번호: 302-17-02708 &nbsp;·&nbsp; 대표: 김성훈<br>\n          주소: 충남 논산시 가야곡면 강청길 32 &nbsp;·&nbsp; 전화: 010-4342-9712',
    '          Yeoyurowa (여유로와) &nbsp;·&nbsp; Business registration no. 302-17-02708 &nbsp;·&nbsp; Owner: Kim Seong-hoon<br>\n          32 Gangcheong-gil, Gayagok-myeon, Nonsan-si, Chungcheongnam-do, South Korea &nbsp;·&nbsp; Tel +82 10-4342-9712')

# ---------- JS ----------
rep("img.onerror = () => { img.src = 'images/hero.jpg'; };", "img.onerror = () => { img.src = '/images/hero.jpg'; };")
rep("img.alt = row.alt || '여유로와 인테리어';", "img.alt = row.alt || 'Yeoyurowa interior';")
rep("{ key: 'exterior', label: '전경' }, { key: 'kitchen', label: '주방' },", "{ key: 'exterior', label: 'Exterior' }, { key: 'kitchen', label: 'Kitchen' },")
rep("{ key: 'living',   label: '거실' }, { key: 'bedroom',  label: '침실' },", "{ key: 'living',   label: 'Living room' }, { key: 'bedroom',  label: 'Bedrooms' },")
rep("{ key: 'bathroom', label: '욕실' }, { key: 'jacuzzi',  label: '자쿠지' },", "{ key: 'bathroom', label: 'Bathrooms' }, { key: 'jacuzzi',  label: 'Jacuzzi' },")
rep("{ key: 'loft',     label: '다락방' },", "{ key: 'loft',     label: 'Loft' },")
rep('사진이 아직 준비 중입니다.', 'Photos coming soon.')


# ---------- CSS ASSET PATHS (page lives at /en/) ----------
rep("background-image: url('images/gallery-01.jpg')", "background-image: url('/images/gallery-01.jpg')")
rep("background-image: url('images/gallery-02.jpg')", "background-image: url('/images/gallery-02.jpg')")
rep("background-image: url('images/interior-living.jpg')", "background-image: url('/images/interior-living.jpg')")
rep("background-image: url('images/gallery-04.jpg')", "background-image: url('/images/gallery-04.jpg')")

# ---------- FACTS BAND ----------
rep('<span class="fact__num">1</span>\n            <span class="fact__label">독채</span>\n            <span class="fact__sub">통째로 단독 사용</span>',
    '<span class="fact__num">1</span>\n            <span class="fact__label">Entire house</span>\n            <span class="fact__sub">Yours alone</span>')
rep('<span class="fact__num">3</span>\n            <span class="fact__label">침실</span>\n            <span class="fact__sub">더블베드 3</span>',
    '<span class="fact__num">3</span>\n            <span class="fact__label">Bedrooms</span>\n            <span class="fact__sub">3 double beds</span>')
rep('<span class="fact__num">2</span>\n            <span class="fact__label">욕실</span>\n            <span class="fact__sub">독립욕실 2개</span>',
    '<span class="fact__num">2</span>\n            <span class="fact__label">Bathrooms</span>\n            <span class="fact__sub">2 separate bathrooms</span>')
rep('<span class="fact__num">10</span>\n            <span class="fact__label">최대 인원</span>\n            <span class="fact__sub">기준 6인 · 1인 추가 2만원</span>',
    '<span class="fact__num">10</span>\n            <span class="fact__label">Max guests</span>\n            <span class="fact__sub">Base 6 · ₩20,000 per extra guest</span>')

# ---------- SKELETONS / MOBILE CTA ----------
rep('<span>예약 캘린더를 불러오는 중입니다</span>', '<span>Loading the booking calendar</span>')
rep('<a href="tel:010-4342-9712" class="mobile-cta__tel">', '<a href="tel:+821043429712" class="mobile-cta__tel">')
rep('      전화 문의\n    </a>', '      Call us\n    </a>')
rep('<a href="#availability" class="mobile-cta__book">예약하기</a>', '<a href="#availability" class="mobile-cta__book">Book now</a>')

# ---------- EATS NEARBY ----------
rep('data-l-all="전체"', 'data-l-all="All"')
rep('data-l-reviews="리뷰 {n}"', 'data-l-reviews="{n} reviews"')
rep('data-l-menu="대표 메뉴"', 'data-l-menu="Popular dishes"')
rep('data-l-parking="주차 가능"', 'data-l-parking="Parking"')
rep('data-l-call="전화 {n}"', 'data-l-call="Call {n}"')
rep('data-l-map="카카오맵에서 보기"', 'data-l-map="View on Kakao Map"')
rep('data-l-empty="해당 분류의 식당이 없습니다."', 'data-l-empty="No places in this category."')
rep('data-l-filter="음식 종류로 거르기"', 'data-l-filter="Filter by food type"')
rep('data-l-rating="별점"', 'data-l-rating="Rating"')
rep('data-l-price="가격대"', 'data-l-price="Price range"')
rep('<h2 class="section-heading reveal reveal-delay-1" id="eats-title">차 한 번 타고,<br><em>주변 맛집</em></h2>',
    '<h2 class="section-heading reveal reveal-delay-1" id="eats-title">One short drive,<br><em>places to eat</em></h2>')
rep('            여유로와에서 가까운 순서로 정리했습니다. 저녁 먹으러 나가는 길에, 돌아오는 길 카페 한 잔에.',
    '            Sorted by distance from the house — for the drive out to dinner, and the coffee on the way back.')

errors = []
for old, new, n in R:
    c = out.count(old)
    if c != n:
        errors.append(f'count {c} != {n}: {old[:70]!r}')
        continue
    out = out.replace(old, new)
if errors:
    print('\n'.join(errors)); sys.exit(1)

# Remaining Hangul outside of allowed spots
allowed = ['김성훈(여유로와)', '(여유로와)', '한국어', '충청남도 논산시 가야곡면 강청길 32', 'aria-label="Korean version"', '"alternateName": "여유로와"',
           'Supabase 동적 이미지 로드', '로컬 hero.jpg 즉시 표시 후 Supabase 이미지로 페이드인 교체', '인테리어 섹션 — interior 슬롯 최대 4장, 없으면 기본 2장 유지',
           'Special offers 이미지', '탭 갤러리', '위치안내', '이용안내', '환불규정']
chk = out
for a in allowed:
    chk = chk.replace(a, '')
leftover = [(i+1, l.strip()[:100]) for i, l in enumerate(chk.split('\n')) if re.search(r'[가-힣]', l)]
if leftover:
    print('LEFTOVER HANGUL:'); [print(x) for x in leftover]; sys.exit(1)

(ROOT / 'en').mkdir(exist_ok=True)
(ROOT / 'en' / 'index.html').write_text(out, encoding='utf-8')
print('OK', len(R), 'replacements ->', ROOT / 'en' / 'index.html', len(out), 'bytes')
