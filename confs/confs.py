def criar_copias_configuracao(mission, id_auv):
    dataset_value = "aris-" + str(mission) + "-auv-" + str(id_auv) + "-data"
    texto_configuracao_base = f"""
conf {{
    dataset =  {dataset_value}
    image_setkeyname = "images" 
    expID =    {dataset_value}
    timef = False
    filter_th = 0
    use_manual_bound = True
}}
train {{
    learning_rate = 5e-4
    learning_rate_alpha = 0.01 
    end_iter = 300000
    start_iter = 0

    warm_up_end = 5000 
    anneal_end = 50000 
    select_valid_px = False

    save_freq = 10
    val_mesh_freq = 10
    report_freq = 1

    igr_weight = 0.1
    variation_reg_weight = 0

    arc_n_samples = 10 
    select_px_method = "bypercent" 
    num_select_pixels = 100
    px_sample_min_weight = 0.001
    randomize_points = True
    percent_select_true = 0.4
    r_div = False 
}}
mesh {{ 
    object_bbox_min = [-7.25, -11.5, -2.25]  
    object_bbox_max = [7.5, 7.0, 2.75]
    x_max = -8,
    x_min = -24,
    y_max = -2.5,
    y_min = -17.5,
    z_max = -13,
    z_min = -19,
    level_set = 0
}}
model {{
    sdf_network {{
        d_out = 65
        d_in = 3
        d_hidden = 64
        n_layers = 4
        skip_in = [2]
        multires = 6
        bias = 1
        scale = 1.0
        geometric_init = False
        weight_norm = True
    }}

    variance_network {{
        init_val = 0.3
    }}

    rendering_network {{
        d_feature = 64
        mode = idr
        d_in = 9
        d_out = 1
        d_hidden = 64
        n_layers = 4
        weight_norm = True
        multires_view = 4
        squeeze_out = True
    }}

    neus_renderer {{
        n_samples = 64 
        n_importance = 0 
        n_outside = 0 
        up_sample_steps = 4    
        perturb = 0
    }}
}}
"""

    nome_arquivo_saida = dataset_value + ".conf"

    try:
        with open(nome_arquivo_saida, "w") as arquivo_saida:
            arquivo_saida.write(texto_configuracao_base)
        print(f"Configuração copiada e alterada com sucesso para '{nome_arquivo_saida}'!")
    except IOError as e:
        print(f"Erro ao criar a cópia da configuração: {e}")

# Exemplo de uso:
for i in range(0,40):
	criar_copias_configuracao(4, i)
