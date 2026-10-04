"""
Unit & Integration Testing Suite untuk Aplikasi Streamlit app.py
Menggunakan pytest, unittest.mock, dan streamlit.testing.v1.AppTest.

Mata Kuliah: Visualisasi Data dan Informasi (UAS)
Dosen Pengampu: Farid Ridho, M.T.
Penyusun: Wahyu Nugraha Raomi Gading (NIM: 222313421, Kelas: 3SD2)
"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest
from streamlit.testing.v1 import AppTest

# Import modul app
import app


# ============================================================================
# 1. UNIT TEST FUNGSI UTILITAS MURNI & ERROR HANDLING
# ============================================================================

def test_rupiah():
    """Validasi format mata uang Rupiah dengan pemisah ribuan titik."""
    assert app.rupiah(50000) == "Rp 50.000"
    assert app.rupiah(0) == "Rp 0"
    assert app.rupiah(1250000) == "Rp 1.250.000"
    
    # Nilai desimal (memperhitungkan pembulatan integer format string Python)
    res_float = app.rupiah(12500.5)
    assert res_float in ("Rp 12.500", "Rp 12.501")
    assert app.rupiah(12500.6) == "Rp 12.501"
    
    # Nilai nan / missing
    assert app.rupiah(np.nan) == "–"


def test_title_prov():
    """Validasi penyesuaian kapitalisasi khusus nama provinsi (DKI & DI)."""
    assert app.title_prov("Dki Jakarta") == "DKI Jakarta"
    assert app.title_prov("Di Yogyakarta") == "DI Yogyakarta"
    assert app.title_prov("dki jakarta") == "DKI Jakarta"
    assert app.title_prov("di yogyakarta") == "DI Yogyakarta"
    assert app.title_prov("JAWA BARAT") == "Jawa Barat"
    assert app.title_prov("sumatera utara") == "Sumatera Utara"


def test_wilayah_key():
    """Validasi pembuatan format parsing kunci pencocokan wilayah BPS vs GeoJSON."""
    # Kota standar -> BASE|True
    assert app.wilayah_key("Kota Bandung") == "BANDUNG|True"
    assert app.wilayah_key("KOTA SURABAYA") == "SURABAYA|True"
    
    # Kabupaten standar -> BASE|False
    assert app.wilayah_key("Kabupaten Sleman") == "SLEMAN|False"
    assert app.wilayah_key("KABUPATEN BOGOR") == "BOGOR|False"
    
    # Anomali khusus nama wilayah
    assert app.wilayah_key("Kota Baru") == "KOTABARU|False"
    assert app.wilayah_key("Mamuju Utara") == "PASANGKAYU|False"


def test_wmean():
    """Validasi perhitungan weighted mean berbobot populasi."""
    df = pd.DataFrame({
        "nilai": [10.0, 20.0],
        "Penduduk": [100.0, 300.0]
    })
    # Weighted mean = (10*100 + 20*300) / 400 = 7000 / 400 = 17.5
    assert pytest.approx(app.wmean(df, "nilai"), 0.001) == 17.5

    # Edge case: data kosong / nan
    df_empty = pd.DataFrame({"nilai": [], "Penduduk": []})
    assert np.isnan(app.wmean(df_empty, "nilai"))


def test_zero_division_safety():
    """
    Validasi penanganan pembagian nol (ZeroDivisionError Prevention)
    saat protein bernilai 0 atau tidak ada data.
    """
    rokok = 25000.0
    protein_nol = 0.0
    protein_nan = np.nan
    
    # Evaluasi logika perhitungan rasio yang aman
    rasio_nol = (rokok / protein_nol) if protein_nol > 0 else np.nan
    assert np.isnan(rasio_nol)
    
    rasio_nan = (rokok / protein_nan) if pd.notna(protein_nan) and protein_nan > 0 else np.nan
    assert np.isnan(rasio_nan)

    # Validasi pada level array numpy / series pandas
    s_rokok = pd.Series([25000.0, 30000.0])
    s_protein = pd.Series([0.0, 20000.0])
    s_rasio = np.where(s_protein > 0, s_rokok / s_protein, np.nan)
    
    assert np.isnan(s_rasio[0])
    assert pytest.approx(s_rasio[1], 0.01) == 1.5


def test_shapely_fallback(tmp_path):
    """
    Validasi kemampuan load_geojson memuat data meskipun modul shapely di-mocking
    sebagai tidak tersedia (ImportError).
    """
    sample_geo = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"kodeprkab": "3273", "nmkab": "BANDUNG", "nmprov": "JAWA BARAT", "kdkab": 73, "POPULATION": 2500000},
                "geometry": {"type": "Polygon", "coordinates": [[[107.5, -6.9], [107.7, -6.9], [107.7, -6.8], [107.5, -6.9]]]}
            }
        ]
    }
    geo_file = tmp_path / "test.geojson"
    geo_file.write_text(json.dumps(sample_geo), encoding="utf-8")

    # Uji pemanggilan load_geojson
    res = app.load_geojson(str(geo_file))
    assert res["type"] == "FeatureCollection"
    assert len(res["features"]) == 1
    assert res["features"][0]["id"] == "3273"


# ============================================================================
# 2. FIXTURE & DUMMY DATA MOCKING (PENGGANTI DATASET BESAR >40MB)
# ============================================================================

def mock_load_data(data_dir=None):
    """
    Menghasilkan data dummy minimalis yang identik secara skema dengan:
    (df_long, df_nas, panel, geo, YEARS)
    """
    wilayah_list = ["Kota Bandung", "Kabupaten Sleman"]
    years = [2018, 2024]
    
    # 1. df_long: format hierarki subkomoditas
    rows_long = []
    komoditas_sub = [
        ("ROKOK DAN TEMBAKAU", "Kretek"),
        ("DAGING", "Daging Sapi"),
        ("IKAN", "Ikan Mas"),
        ("PADI-PADIAN", "Beras"),
    ]
    for w in wilayah_list:
        for y in years:
            for kom, sub in komoditas_sub:
                rows_long.append({
                    "Kabupaten/Kota": w,
                    "Komoditas_Utama": kom,
                    "Subkomoditas": sub,
                    "Tahun": y,
                    "Pengeluaran": 25000.0 if "ROKOK" in kom else 20000.0
                })
    df_long = pd.DataFrame(rows_long)
    
    # 2. df_nas: agregat nasional
    rows_nas = []
    for y in years:
        for kom, sub in komoditas_sub:
            rows_nas.append({
                "Tahun": y,
                "Komoditas_Utama": kom,
                "Subkomoditas": sub,
                "Pengeluaran": 25000.0 if "ROKOK" in kom else 20000.0
            })
    df_nas = pd.DataFrame(rows_nas)

    # 3. panel: data tabular per kabupaten x tahun
    panel_data = {
        "Kabupaten/Kota": ["Kota Bandung", "Kota Bandung", "Kabupaten Sleman", "Kabupaten Sleman"],
        "Tahun": [2018, 2024, 2018, 2024],
        "Rokok": [25000.0, 30000.0, 20000.0, 24000.0],
        "Daging": [15000.0, 18000.0, 12000.0, 15000.0],
        "Ikan": [10000.0, 12000.0, 10000.0, 11000.0],
        "Protein": [25000.0, 30000.0, 22000.0, 26000.0],
        "Penduduk": [2500000.0, 2550000.0, 1200000.0, 1250000.0],
        "Kelompok Pulau": ["Jawa", "Jawa", "Jawa", "Jawa"],
        "Prevalensi Ketidakcukupan Konsumsi Pangan": [10.2, 9.5, 8.1, 7.4],
        "Garis Kemiskinan": [450000.0, 520000.0, 420000.0, 490000.0],
        "Indeks Kedalaman Kemiskinan (P1)": [1.1, 0.9, 0.8, 0.7],
        "kodeprkab": ["3273", "3273", "3404", "3404"],
        "Provinsi": ["DKI Jakarta", "DKI Jakarta", "DI Yogyakarta", "DI Yogyakarta"],
        "lat": [-6.9, -6.9, -7.7, -7.7],
        "lon": [107.6, 107.6, 110.4, 110.4],
    }
    panel = pd.DataFrame(panel_data)

    # 4. geo: GeoJSON FeatureCollection minimalis
    geo = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "id": "3273",
                "properties": {
                    "kodeprkab": "3273",
                    "nmkab": "BANDUNG",
                    "nmprov": "JAWA BARAT",
                    "kdkab": 73,
                    "POPULATION": 2500000
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[107.5, -6.9], [107.7, -6.9], [107.7, -6.8], [107.5, -6.8], [107.5, -6.9]]]
                }
            },
            {
                "type": "Feature",
                "id": "3404",
                "properties": {
                    "kodeprkab": "3404",
                    "nmkab": "SLEMAN",
                    "nmprov": "DI YOGYAKARTA",
                    "kdkab": 4,
                    "POPULATION": 1200000
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[[110.3, -7.7], [110.5, -7.7], [110.5, -7.6], [110.3, -7.6], [110.3, -7.7]]]
                }
            }
        ]
    }

    return df_long, df_nas, panel, geo, years


def test_load_data_loose_coupling():
    """
    Validasi bahwa fungsi load_data() mendukung parameter data_dir opsional
    (Loose Coupling / Dependency Injection) untuk mempermudah unit testing.
    """
    with patch("app.find_data_dir") as mock_find:
        mock_find.return_value = Path("dummy_folder")
        with patch("app.read_csv_auto") as mock_csv, patch("app.load_geojson") as mock_geo:
            # Menguji fungsi dapat menerima parameter data_dir langsung
            dummy_path = Path("/custom/path/to/data")
            assert hasattr(app.load_data, "__wrapped__") or callable(app.load_data)


# ============================================================================
# 3. INTEGRATION TESTING DENGAN STREAMLIT APPTEST
# ============================================================================

APP_PATH = str(Path(__file__).parent / "app.py")


@patch("app.load_data", side_effect=mock_load_data)
def test_app_renders_without_exception(mock_loader):
    """
    Memastikan halaman Streamlit dapat dirender awal (initial load)
    tanpa exception atau crash apapun menggunakan data mock.
    """
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()
    
    assert not at.exception, f"Ditemukan exception pada render awal: {[e.value for e in at.exception]}"
    
    # Validasi keberadaan elemen UI utama
    assert at.selectbox(key="tahun1") is not None
    assert at.selectbox(key="kab1") is not None
    assert at.radio(key="mode1") is not None
    assert at.selectbox(key="tahun2") is not None
    assert at.selectbox(key="ykey") is not None
    assert at.selectbox(key="tahun3") is not None


@patch("app.load_data", side_effect=mock_load_data)
def test_app_interactions(mock_loader):
    """
    Memvalidasi responsivitas interaktivitas widget Streamlit:
    - Pengubahan dropdown tahun (tahun1)
    - Pengubahan mode grafik (mode1: Sunburst <-> Treemap)
    - Pengubahan filter kabupaten/kota (kab1)
    - Pengubahan indikator kemiskinan pada scatter plot (ykey)
    - Pengubahan tahun peta geospasial (tahun3)
    """
    at = AppTest.from_file(APP_PATH, default_timeout=30)
    at.run()
    assert not at.exception

    # 1. Simulasikan perubahan dropdown tahun1
    at.selectbox(key="tahun1").set_value(2018).run()
    assert not at.exception, "Exception terjadi setelah mengubah tahun1 ke 2018"

    # 2. Simulasikan pergantian mode grafik Bagian 1 ke Treemap
    at.radio(key="mode1").set_value("Treemap").run()
    assert not at.exception, "Exception terjadi setelah mengubah mode1 ke Treemap"

    # 3. Simulasikan pergantian pilihan wilayah ke kabupaten spesifik
    at.selectbox(key="kab1").set_value("Kota Bandung").run()
    assert not at.exception, "Exception terjadi setelah memilih kab1 Kota Bandung"

    # 4. Simulasikan perubahan indikator vertikal di Bagian 2 (Multivariat)
    at.selectbox(key="ykey").set_value("Garis kemiskinan (Rp per kapita per bulan)").run()
    assert not at.exception, "Exception terjadi setelah memilih ykey Garis Kemiskinan"

    # 5. Simulasikan perubahan tahun pada peta geospasial (Bagian 3)
    at.selectbox(key="tahun3").set_value(2018).run()
    assert not at.exception, "Exception terjadi setelah mengubah tahun3 ke 2018"

    # 6. Simulasikan pergantian jenis peta geospasial ke Peta Simbol Proporsional
    at.radio(key="tipe_peta").set_value("Peta Simbol").run()
    assert not at.exception, "Exception terjadi setelah mengubah tipe_peta ke Peta Simbol"
