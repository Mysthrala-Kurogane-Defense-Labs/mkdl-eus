# MKDL euskaraz

Euskarazko landing-a: https://mkdl.eus/.
Jatorria: Mysthrala-Kurogane-Defense-Labs/mysthrala-kurogane-defense-labs.github.io.
Diseinua eta marka mantendu dira. Lege-orriak eta adibideko dokumentuak gaztelaniaz daude, esteketan adierazita.

## Argitaratzea

GitHub Pages, main adarreko Actions workflow-aren bidez. Cloudflare DNS.
`py -3 scripts/package-site.py --target github` komandoak fitxategi publikoak, estekak eta aingurak egiaztatzen ditu.
`wrangler.jsonc` prestaketa alternatiboa da; ez da ekoizpeneko hedapena.

## 2026-11-05

Erabiltzaileak euskarazko bertsioa, erakundeko biltegia eta mkdl.eus domeinuko hedapena baimendu ditu.
Cloudflare zona aktiboa eta web DNS erregistrorik gabe egiaztatu da.
Wrangler autentifikazioa iraungita dago; cf saioak DNS baimenak ditu, Workers idazketa-baimenik gabe.
Hedapena GitHub Pages bidez egiten da. Ez da posta edo bestelako zerbitzurik aldatu.
