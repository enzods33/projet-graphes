"""
Init du module interactions_canvas

Regroupe et expose toutes les fonctions principales de gestion du canvas,
points, zoom, événements et cache pour l'application de graphes.
"""

from .canvas_init import (
    set_canvas,
    save_callback,
    reset_callbacks,
    reset,
    set_counter_label,
    set_zoom_label,
    full_reset_view,
    apply_parameters_if_possible,
    change_graph
)

from .sommets import (
    put_logic_point,
    draw_point,
    redraw_canvas,
    update_edge,
    update_counter_label,
)

from .zoom import (
    zoom_in,
    zoom_out,
    refresh_scrollregion,
    update_zoom_label,
    apply_intial_global_factor,
)

from .evenements import (
    is_drag,
    on_drag_start,
    on_drag_motion,
    on_drag_end,
    on_right_click
)

from .cache_distance import (
    get_real_distance,
    add_to_cache,
    remove_edges,
    get_all_edges
)
