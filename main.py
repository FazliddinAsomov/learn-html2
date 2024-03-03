
<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Web dasturchi uchun portfolio</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Portfolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Bosh sahifa <span class="sr-only">(hozirgi)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Biz haqimizda</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Xizmatlar</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Aloqa</a>
      </li>
    </ul>
  </div>
</nav>

<!-- Header -->
<header class="jumbotron jumbotron-fluid">
  <div class="container">
    <h1 class="display-4">Assalomu alaykum</h1>
    <p class="lead">Men web dizaynerman va sizning loyihalarizni amalga oshirishga tayyorman. Mavjud web saytlarimizni o'rganing va biz bilan bog'laning.</p>
  </div>
</header>

<!-- About Section -->
<section id="about" class="container">
  <div class="row">
    <div class="col-md-6">
      <h2>Biz haqimizda</h2>
      <p>Bizning kompaniyamiz 10 yildan ortiq tajriba bilan web dizayn va rivojlanish sohasida faoliyat ko'rsatmoqda.</p>
      <p>Sizning loyihalaringizni rivojlantirishga va to'liq ta'minlashga tayyormiz.</p>
    </div>
    <div class="col-md-6">
      <img src="https://proforientator.ru/upload/iblock/4cb/4cbc376b07f094452802c29a37728eba.jpg" alt="Biz haqimizda" class="img-fluid">
    </div>
  </div>
</section>

<!-- Services Section -->
<section id="services" class="container">
  <h2>Xizmatlar</h2>
  <div class="row">
    <div class="col-md-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Veb Dizayn</h5>
          <p class="card-text">Ilova interfeysi, grafik dizayn va boshqa xizmatlar.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Veb rivojlanishi</h5>
          <p class="card-text">Ilova rivojlanishi va boshqa texnologiyalar.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Mobil rivojlanishi</h5>
          <p class="card-text">iOS va Android uchun ilovalarni rivojlantirish.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Portfolio Section -->
<section id="portfolio" class="container">
  <h2>Portfolio</h2>
  <div class="row">
    <div class="col-md-4">
      <div class="card">
        <img src="data:image/png;base64,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" class="card-img-top" alt="Loyiha 1">
        <div class="card-body">
          <h5 class="card-title">Loyiha 1</h5>
          <p class="card-text">Bu bizning birinchi loyihamiz.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card">
        <img src="https://blog.hubspot.com/hs-fs/hubfs/image8-2.jpg?width=600&name=image8-2.jpg" class="card-img-top" alt="Loyiha 2">
        <div class="card-body">
          <h5 class="card-title">Loyiha 2</h5>
          <p class="card-text">Bu bizning ikkinchi loyihamiz.</p>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card">
        <img src="data:image/png;base64,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" class="card-img-top" alt="Loyiha 3">
        <div class="card-body">
          <h5 class="card-title">Loyiha 3</h5>
          <p class="card-text">Bu bizning uchunchi loyihamiz.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Contact Section -->
<section id="contact" class="container">
  <h2>Aloqa</h2>
  <p>Agar siz biz bilan bog'lanishni xohlasangiz.
  </p>
  <p>Telefon raqam +998 93-586-06-59</p>
  <p>Email fazliddin71539@gmail.com</p>
  <form>
    <div class="form-group">
      <label for="name">Ismingiz</label>
      <input type="text" class="form-control" id="name" placeholder="Ismingizni kiriting">
    </div>
    <div class="form-group">
      <
