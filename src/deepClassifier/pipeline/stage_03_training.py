from deepClassifier.config import ConfigurationManager
from deepClassifier.entity.config_entity import PrepareCallbacksConfig, TrainingConfig
from deepClassifier.components import PrepareCallbacks, Training

try:
    config = ConfigurationManager()
    prepare_callbacks_config = config.get_prepare_callbacks_config()
    prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks()  

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_validation_generator()
    training.train(
        callbacks_list=callback_list
    ) 
except Exception as e:
    raise e