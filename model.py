import lightning as L
import torch
import torch.nn as nn, torch.optim as optim


class pretrainedModel(L.LightningModule):
    def __init__(
        self, pre_trained_model, 
        last_layer_classifier, 
        loss_fn=nn.BCEWithLogitsLoss, 
        optimizer=optim.Adam, 
        log_step_loss : bool = True,
        **optimizer_params
    ):
        super().__init__()
        self.features = nn.Sequential(*list(pre_trained_model.children())[:-1])
        self.class_classifier = last_layer_classifier
        self.loss_fn = loss_fn()
        self.optimizer = optimizer
        self.optimizer_params = optimizer_params
        self.log_step_loss = log_step_loss

    def forward(self, x):
        return self.class_classifier(self.features(x).view(x.size(0), -1))

    def configure_optimizers(self):
        return self.optimizer(self.parameters(), **self.optimizer_params)
    
    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        if self.log_step_loss:
            self.log("train_loss", loss, prog_bar=True, on_epoch=True)
        return loss

    def test_step(self, batch, batch_idx):
        """
        Defines the testing loop for each batch.

        Parameters
        ----------
        batch
            The input batch.
        batch_idx
            The index of the current batch.

        Returns
        -------
        The loss value for the current batch.
        """
        x, y = batch
        predictions = self(x)
        loss = self.loss_fn(predictions.view(y.size()), y)
        if self.logging:
            self.log("test_loss", loss, prog_bar=True, on_step=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = self.loss_fn(y_hat, y)
        if self.log_step_loss:
            self.log("val_loss", loss, prog_bar=True, on_step=True)
        return loss

    def predict_step(self, batch, batch_idx):
        """
        Perform a forward pass through the model to make predictions.

        Args:
            batch: The input batch of data.
            batch_idx: The index of the current batch.

        Returns:
            The predicted output of the model.
        """
        x, y = batch
        return self(x)
