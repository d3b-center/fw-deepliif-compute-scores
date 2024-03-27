# DeepLIIF calculate scores

Flywheel gear that calculates scores based on [DeepLIIF](https://github.com/nadeemlab/DeepLIIF/tree/main) model-generated IHC images. See also https://deepliif.org/

### Dependencies

- Python 3.8
- DeepLIIF

### Settings

Required inputs:
- image
- refined segmentation
- marker (optional)

Optional configuration:
- segmentation threshold (default: 150)
- size threshold (default: auto)
- size threshold - upper (default: none)
- marker threshold (default: auto)
- resolution (default: None/40x)

### References

https://www.nature.com/articles/s42256-022-00471-x.epdf?sharing_token=TfIQdFzqGrYolrSS_NyOJtRgN0jAjWel9jnR3ZoTv0P90KdmGq_lkIuepQpaAnx9M_HMX0dkqP8OF91EhA0P9AAsgUeGoCtaqab2DQMx50ft_LVCW8JvZUJ-qQxqZjpYLSzzUo00YLH8PJ-XBckUsuikhsZl8LQ1us1rXPrAWKE%3D
